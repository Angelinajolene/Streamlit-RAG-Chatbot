# Streamlit RAG Chatbot

A Retrieval‑Augmented Generation (RAG) chatbot built with Streamlit, ChromaDB, and Google Gemini 2.5 Flash.
This application allows users to upload a PDF or DOCX file, automatically extracts and chunks the text, stores embeddings in ChromaDB, 
and answers questions strictly based on the uploaded document.

##  Table of Contents
* [Description](#-description)
* [Features](#-features)
* [Project Architecture](#-project-architecture)
* [Installation](#%EF%B8%8F-installation)
* [Environment Setup](#%EF%B8%8F-environment-setup)
* [Usage](#%EF%B8%8F-usage)
* [Acknowledgements](#-acknowledgements)

## Description
The Streamlit RAG Chatbot demonstrates how to build a document‑aware assistant using RAG.
It combines semantic search (via embeddings + ChromaDB) with generative AI (Google Gemini) to provide accurate answers from uploaded documents

##  Features
* **Multi-Format Support:** Easily upload and parse both `.pdf` and `.docx` files.
* **Fast Text Extraction:** Uses optimized extraction libraries (`PyMuPDF` and `python-docx`).
* **Smart Chunking:** Employs LangChain's `RecursiveCharacterTextSplitter` with token overlaps to maintain contextual integrity.
* **Local Embeddings:** Utilizes the highly-efficient `all-MiniLM-L6-v2` Sentence Transformer entirely offline.
* **Vector Storage:** Manages state and context chunks using an integrated `ChromaDB` persistent local client.
* **Strict Context Control:** System prompts force the Gemini LLM to answer *only* from the extracted document data.
* **Modern UI:** Built on Streamlit with intuitive loading spinners, clean metrics, and responsive error handling.

##  Installation

### Prerequisites
* Python 3.9 or higher installed on your machine.
* A Google Gemini API Key.
Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/streamlit-rag-chatbot.git](https://github.com/your-username/streamlit-rag-chatbot.git)
   cd streamlit-rag-
   
2. ## Create a virtual environment:

  * On Windows:
     python -m venv venv
     venv\Scripts\activate
   
  * On macOS/Linux:
     python -m venv venv
     source venv/bin/activate
   
4. ## Install the dependencies:
    pip install -r requirements.txt


## Environment Setup
Create a file named .env in the root directory of your project and insert your Gemini API key:
Code snippet
GOOGLE_API_KEY=your_actual_gemini_api_key_here

## To Run
To start your local development server, run the following command in your terminal:
Bash
streamlit run app.py

## How to use the app:
Upload: Drag and drop your target PDF or DOCX file into the Streamlit sidebar/uploader.

Process: Wait a brief moment for the UI to display success badges confirming text extraction and database storage.

Query: Type your question into the text input bar.

Retrieve: Click "Get Answer" to fetch the relevant sections and watch Gemini synthesize a strict context-driven response.

## Acknowledgements

Streamlit — For the fast, intuitive UI layer.

ChromaDB — For seamless local vector management.

Hugging Face SentenceTransformers — For embedding models.

Google GenAI SDK — For the powerful Gemini 2.5 generative engine.
