from langchain_core.documents import Document
from app.pipeline.chunker import chunk_documents

def test_chunk_documents():
    docs = [Document(page_content="Texto " * 100)]
    chunks = chunk_documents(docs)

    assert len(chunks) > 1
    assert all(c.page_content.strip() for c in chunks)
