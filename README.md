# Streamlit RAG Chatbot

A Retrieval‑Augmented Generation (RAG) chatbot built with Streamlit, ChromaDB, and Google Gemini 2.5 Flash.
This application allows users to upload a PDF or DOCX file, automatically extracts and chunks the text, stores embeddings in ChromaDB, 
and answers questions strictly based on the uploaded document.

## Table of Contents

Description
Features
Installation
Environment Variables
Usage
Project Structure
Contributing
License
Acknowledgements

## Description
The Streamlit RAG Chatbot demonstrates how to build a document‑aware assistant using RAG.
It combines semantic search (via embeddings + ChromaDB) with generative AI (Google Gemini) to provide accurate answers from uploaded documents

## Features
File Upload: Supports PDF and DOCX formats.

Text Extraction: Extracts text using PyMuPDF (fitz) and python-docx.

Chunking: Splits text into overlapping chunks for better retrieval.

Embeddings: Uses sentence-transformers/all-MiniLM-L6-v2.

Vector Database: Stores chunks in ChromaDB.

Context Retrieval: Retrieves top 3 relevant chunks for a query.

Answer Generation: Uses Google Gemini 2.5 Flash to generate answers strictly from context.

Streamlit UI: Simple interface with spinners, success messages, and results display.

### Installation
Prerequisites
Python 3.9+

A Google API key (Gemini) stored in .env
1. Clone the repository
git clone https://github.com/your-username/streamlit-rag-chatbot.git
cd streamlit-rag-chatbot

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

## Environment Variables
Create a .env file in the project root:
[GOOGLE_API_KEY=your_api_key_here]

## Usage
Run the Streamlit app:
[streamlit run app.py]

1. Upload a PDF/DOCX file.
2. Wait for text extraction, chunking, and embedding storage.
3. Type a question in the input box.
4. Get an answer generated from the document context.

## Acknowledgements
Streamlit
ChromaDB
SentenceTransformers
Google Gemini
LangChain Text Splitters


