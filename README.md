📘 Wikipedia-based RAG Assistant

Retrieval-Augmented Generation using Wikipedia as Knowledge Base

📌 Project Overview

This project implements a Retrieval-Augmented Generation (RAG) assistant using the Wikipedia article on Retrieval-Augmented Generation as its knowledge source.

The goal is to demonstrate how combining document retrieval with large language models (LLMs) helps generate factually grounded responses, reducing hallucinations commonly seen in standalone LLMs.

This project was built as part of Module 1 – Foundations of Agentic AI for the Agentic AI Developer Certification (Ready Tensor).

🧠 Problem Statement

Large Language Models rely on static training data and may hallucinate when answering factual or domain-specific questions. This is especially problematic for educational and knowledge-intensive applications.

Retrieval-Augmented Generation (RAG) addresses this limitation by retrieving relevant external documents at inference time and injecting them into the model’s prompt, ensuring responses are grounded in authoritative sources.

🏗️ System Architecture

The system follows a standard RAG pipeline:

Wikipedia content is loaded from a local text file

The content is split into overlapping semantic chunks

Each chunk is converted into vector embeddings

Embeddings are stored in a vector database (ChromaDB)

At query time, relevant chunks are retrieved using semantic search

An LLM generates answers using the retrieved context

This design ensures responses are based on retrieved source material rather than the model’s internal knowledge alone.

🛠️ Tech Stack

Python

LangChain

ChromaDB (vector database)

Sentence-Transformers (embeddings)

OpenAI GPT models (LLM)

Wikipedia (knowledge source)

📂 Project Structure
wikipedia-rag-assistant/
├── app.py                  # Main RAG pipeline
├── ingest.py               # Wikipedia loading and chunking
├── vectordb.py             # Vector database creation
├── prompts.py              # Prompt templates
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── .env.example            # Environment variable template
└── data/
    └── rag_wikipedia.txt   # Wikipedia article content

⚙️ Setup Instructions (Optional)

⚠️ Running the project locally is optional for evaluation.
The code structure and logic are sufficient for review.

If you want to run it locally:

1️⃣ Clone the Repository
git clone https://github.com/jhahimanshu1996-sketch/wikipedia-rag-assistant.git
cd wikipedia-rag-assistant

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables
cp .env.example .env


Add your OpenAI API key to .env:

OPENAI_API_KEY=your_api_key_here

5️⃣ Run the Assistant
python app.py

💬 Sample Interaction

User:
What is retrieval-augmented generation?

Assistant:
Retrieval-augmented generation enhances large language models by retrieving relevant external documents and incorporating them into the prompt before generating a response, improving factual accuracy and grounding.

User:
Why is RAG useful for LLMs?

Assistant:
RAG helps mitigate hallucinations by supplying relevant external context at inference time, allowing the model to generate responses based on authoritative source material.

⚠️ Limitations

The knowledge base is limited to a single Wikipedia article

Responses do not currently include explicit source citations

Retrieval quality depends on chunking and embedding strategy

These limitations were intentionally accepted to keep the project focused on core RAG fundamentals.

🚀 Future Improvements

Ingest multiple documents or Wikipedia pages

Add source attribution for retrieved chunks

Implement hybrid retrieval (BM25 + vector search)

Expose the assistant via a REST API or web UI

Add evaluation metrics for retrieval quality

📎 Code Availability

This repository contains the complete implementation of the project, including all scripts, configuration files, and documentation required to understand and reproduce the RAG pipeline.
