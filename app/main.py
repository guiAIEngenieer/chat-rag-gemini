from app.settings import PDF_DIRECTORY
from app.config.constants import SESSION_ID
from app.pipeline.ingest import run_ingest
from app.session.manager import manager
from app.rag.chain import build_chat_chain
from app.utils.validation import validate_prompt
from app.core.logger import logger

def main():
    vectorstore = run_ingest(PDF_DIRECTORY)
    chat_chain, retriever = build_chat_chain(vectorstore, manager)

    while True:
        question = input("prompt: ").strip()

        if question.lower() == "sair":
            break

        error = validate_prompt(question)
        
        if error:
            logger.error(error)
            continue

        context = manager.get_context(
                question, retriever
            )

        response = chat_chain.invoke(
            {"question": question, "context": context},
            config={"configurable": {"session_id": SESSION_ID}}
        )

        logger.info(f"\nLLM: {response.content}\n")

if __name__ == "__main__":
    main()
