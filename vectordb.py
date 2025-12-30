from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_db(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    vectordb.persist()
    return vectordb
