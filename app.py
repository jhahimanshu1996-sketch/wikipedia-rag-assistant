import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from ingest import load_and_chunk_wikipedia
from vectordb import create_vector_db
from prompts import RAG_PROMPT

load_dotenv()

def build_rag_pipeline():
    # Step 1: Load and chunk data
    chunks = load_and_chunk_wikipedia("data/rag_wikipedia.txt")

    # Step 2: Create vector DB
    vectordb = create_vector_db(chunks)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # Step 3: LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    # Step 4: QA Chain
    qa_chain = LLMChain(
        llm=llm,
        prompt=RAG_PROMPT
    )

    return retriever, qa_chain

def ask_question(question):
    retriever, qa_chain = build_rag_pipeline()

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    response = qa_chain.run(
        context=context,
        question=question
    )

    return response

if __name__ == "__main__":
    print("🔹 RAG Wikipedia Assistant 🔹")
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        answer = ask_question(q)
        print("\nAnswer:\n", answer)
