# 🤖 AI Resume Chatbot

An AI-powered resume assistant that allows recruiters and hiring managers to interact with my resume through a conversational interface.

The chatbot uses Retrieval-Augmented Generation (RAG) to answer questions about my professional experience, technical skills, projects, and education.

## Features

- 📄 Resume parsing from PDF
- 🔍 Semantic search using Hugging Face embeddings
- 🗂 Vector storage with ChromaDB
- 🤖 AI-powered responses using Google Gemini
- 💬 Interactive Streamlit chatbot interface
- 🚫 Hallucination reduction through resume-based retrieval
- ⚡ Fast and recruiter-friendly experience

## Tech Stack

### Frontend
- Streamlit

### LLM
- Google Gemini

### Embeddings
- Hugging Face Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- ChromaDB

### Backend
- Python

### Document Processing
- PyPDF

## Architecture

Resume PDF
↓
Text Extraction
↓
Section-based Chunking
↓
Hugging Face Embeddings
↓
ChromaDB Vector Store
↓
Relevant Context Retrieval
↓
Gemini LLM
↓
Natural Language Response

## Example Questions

- What technical skills does Vikas have?
- What cloud technologies has he worked with?
- Tell me about his professional experience.
- What AI/LLM projects has he built?
- What programming languages does he know?

## Installation

Clone the repository:

```bash
git clone https://github.com/dvikasku/resume-chatbot.git

cd resume-chatbot
