from langchain_core.documents import Document
from app.pipeline.vectorstore import build_faiss
from langchain.embeddings.base import Embeddings

class FakeEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [[0.0] * 3072 for _ in texts]

    def embed_query(self, text):
        return [0.0] * 3072

def test_build_faiss(monkeypatch):
    docs = [Document(page_content="Teste")]

    monkeypatch.setattr(
        "app.pipeline.vectorstore.GoogleGenerativeAIEmbeddings",
        lambda *args, **kwargs: FakeEmbeddings()
    )

    vs = build_faiss(docs)

    assert vs.index.ntotal == 1
