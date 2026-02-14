from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.constants import CHUNK_OVERLAP , CHUNK_SIZE
from app.core.logger import logger

def chunk_documents(documents):
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size= CHUNK_SIZE,
            chunk_overlap= CHUNK_OVERLAP,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        return splitter.split_documents(documents)

    except Exception:
        logger.exception(f"ERROR chunker.py (chunk_documents)")
        raise