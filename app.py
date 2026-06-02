import streamlit as st
import fitz
from docx import Document
from dotenv import load_dotenv
import os
import shutil

from google import genai

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb


load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found in .env")
    st.stop()



client = genai.Client(api_key=API_KEY)



@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

embedding_model = load_embedding_model()



CHROMA_PATH = "chroma_db"

client_db = chromadb.PersistentClient(
    path=CHROMA_PATH
)


st.set_page_config(
    page_title="RAG Chatbot",
    layout="wide"
)

st.title(" RAG PDF / DOCX Chatbot")
st.write("Upload a PDF or DOCX and ask questions.")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["pdf", "docx"]
)



def extract_pdf_text(file):

    pdf = fitz.open(
        stream=file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    return text



def extract_docx_text(file):

    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text



def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    return chunks



def store_chunks(chunks):

    try:
        client_db.delete_collection("document_chunks")
    except:
        pass

    collection = client_db.create_collection(
        name="document_chunks"
    )

    embeddings = embedding_model.encode(
        chunks
    ).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return collection



def retrieve_context(
    question,
    collection
):

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]

    return docs



def ask_gemini(
    question,
    context
):

    prompt = f"""
You are a helpful assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text



if uploaded_file:

    with st.spinner("Extracting text..."):

        if uploaded_file.name.endswith(".pdf"):
            text = extract_pdf_text(
                uploaded_file
            )
        else:
            text = extract_docx_text(
                uploaded_file
            )

    st.success("Text Extracted")

    chunks = create_chunks(text)

    st.write(
        f"Chunks Created: {len(chunks)}"
    )

    with st.spinner(
        "Creating embeddings and storing in ChromaDB..."
    ):

        collection = store_chunks(chunks)

    st.success(
        "Stored Successfully in ChromaDB"
    )

    question = st.text_input(
        "Ask a Question"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning(
                "Enter a question"
            )
            st.stop()

        with st.spinner(
            "Retrieving context..."
        ):

            docs = retrieve_context(
                question,
                collection
            )

            context = "\n\n".join(docs)

        with st.spinner(
            "Generating answer..."
        ):

            answer = ask_gemini(
                question,
                context
            )

        st.subheader("Answer")

        st.write(answer)

        