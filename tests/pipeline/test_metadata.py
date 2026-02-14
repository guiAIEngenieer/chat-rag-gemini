from langchain_core.documents import Document
from app.pipeline.metadata import auto_title, enrich_metadata

def test_auto_title():
    docs = [Document(page_content="Titulo\nConteudo")]
    assert auto_title(docs) == "TITULO"

def test_enrich_metadata():
    chunks = [Document(page_content="A"), Document(page_content="B")]

    enriched = enrich_metadata(chunks, "arquivo.pdf", "TESTE")

    assert enriched[0].metadata["chunk_id"] == 0
    assert enriched[1].metadata["chunk_id"] == 1
    assert enriched[0].metadata["title"] == "TESTE"
