# Wikipedia-based RAG Assistant

This project implements a Retrieval-Augmented Generation (RAG) assistant using
the Wikipedia page on Retrieval-Augmented Generation as its knowledge source.

## How it Works
1. Wikipedia content is loaded and chunked
2. Text chunks are embedded using Sentence Transformers
3. Embeddings are stored in ChromaDB
4. Relevant chunks are retrieved at query time
5. A language model generates grounded answers

## Tech Stack
- LangChain
- ChromaDB
- Sentence Transformers
- OpenAI GPT

## Run Instructions
1. Add your API key in `.env`
2. Install dependencies:

pip install -r requirements.txt
3. Run:

python app.py

## Example Use Cases
- Understanding RAG fundamentals
- Educational Q&A assistant
- Reference-based AI systems
