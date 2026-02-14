from operator import itemgetter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableWithMessageHistory
from app.config.constants import DEFAULT_TEMPERATURE , CHAT_MODEL
from app.session.manager import manager
from app.core.logger import logger
from .prompts import RAG_PROMPT
from .retriever import build_retriever

def build_chat_chain(vectorstore, session_manager):
    try:
        llm = ChatGoogleGenerativeAI(
            model= CHAT_MODEL,
            temperature= DEFAULT_TEMPERATURE
        )

        retriever = build_retriever(vectorstore)

        rag_chain = (
            {
                "context": itemgetter("context"),
                "question": itemgetter("question"),
                "history": itemgetter("history"),
            }
            | RAG_PROMPT
            | llm
        )

        chat_chain = RunnableWithMessageHistory(
            rag_chain,
            manager.session_history,
            input_messages_key="question",
            history_messages_key="history"
        )

        return chat_chain, retriever
    
    except Exception:
        logger.exception(f"ERROR chain.py (build_chat_chain)")
        raise