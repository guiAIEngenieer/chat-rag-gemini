import os
import faiss
from uuid import uuid4
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config.constants import DIMENSION, NEIGHBORS, EMBEDDING_MODEL , FAISS_PATH
from app.core.logger import logger


def create_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )


def load_vectorstore_if_exists():
    if os.path.exists(FAISS_PATH):

        try:
            embeddings = create_embeddings()

            vectorstore = FAISS.load_local(
                FAISS_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )

            return vectorstore

        except Exception as e:
            logger.exception(f"ERROR vectorstore.py (load_vectorstore_if_exists): {e}")
            raise

    return None


def build_faiss(chunks):
    if not chunks:
        logger.error("ERROR : No chunks received for indexing.")
        raise

    try:
        embeddings = create_embeddings()

        index = faiss.IndexHNSWFlat(DIMENSION, NEIGHBORS)

        vectorstore = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )

        ids = [str(uuid4()) for _ in chunks]

        vectorstore.add_documents(chunks, ids=ids)

        vectorstore.save_local(FAISS_PATH)

        return vectorstore

    except Exception:
        logger.exception(f"ERROR vectorstore.py (build_faiss)")
        raise

def get_or_create_vectorstore(chunks):

    vectorstore = load_vectorstore_if_exists()

    if vectorstore is not None:
        return vectorstore

    return build_faiss(chunks)
