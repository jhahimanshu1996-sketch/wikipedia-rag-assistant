from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_wikipedia(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)
    return chunks
