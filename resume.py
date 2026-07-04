from pypdf import PdfReader
import re
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
from sentence_transformers import SentenceTransformer
import chromadb
import streamlit as st

def load_resume():
    reader = PdfReader("resume.pdf")
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def create_chunks(text):
    sections = re.split(
        r'\n\s*(?=[A-Z][A-Z\s]{3,}\n)',
        text
    )
    return [
        section.strip()
        for section in sections
        if section.strip()
    ]

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="resume"
)


def create_vector_db(chunks):

    if collection.count() > 0:
        return

    for i, chunk in enumerate(chunks):

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding]
        )

def retrieve_context(question):

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return "\n".join(
        results["documents"][0]
    )

def ask_resume(question):

    context = retrieve_context(question)

    prompt = f"""
You are Vikas's AI Resume Assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

If not found, say:
'I could not find that information in the resume.'
"""

    response = model.generate_content(
        prompt
    )

    return response.text


st.title("Vikas Resume Chatbot")


if "loaded" not in st.session_state:

    text = load_resume()

    chunks = create_chunks(text)

    create_vector_db(chunks)

    st.session_state.loaded = True

question = st.text_input(
    "Ask a question about my resume"
)

if question:

    answer = ask_resume(question)

    st.write(answer)