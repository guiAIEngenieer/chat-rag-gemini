from langchain_community.document_loaders import PyPDFLoader
from .loader import load_pdfs
from .chunker import chunk_documents
from .metadata import auto_title, enrich_metadata
from .vectorstore import get_or_create_vectorstore
from app.core.logger import logger


def run_ingest(pdf_directory):
    all_chunks = []

    try:
        for pdf in load_pdfs(pdf_directory):
            documents = PyPDFLoader(pdf).load()
            chunks = chunk_documents(documents)

            if not chunks:
                continue

            title = auto_title(documents)
            chunks = enrich_metadata(chunks, pdf, title)
            all_chunks.extend(chunks)

        return get_or_create_vectorstore(all_chunks)

    except Exception:
        logger.exception(f"ERROR ingest.py (run_ingest)")
        raise
