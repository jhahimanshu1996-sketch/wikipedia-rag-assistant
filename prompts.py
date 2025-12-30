from langchain.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant that answers questions using only the context provided.

Context:
{context}

Question:
{question}

Answer clearly and factually. If the answer is not in the context, say you do not know.
"""
)
