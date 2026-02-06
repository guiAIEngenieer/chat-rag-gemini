from api_connections import gemini_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from operator import itemgetter
from pipeline import faiss_db
import os


# Funçaõ de verificação de historico existente
context_store = {}
def get_or_create_context(session_id: str, question: str):
    if session_id not in context_store:
        docs = retriever.invoke(question)
        context_store[session_id] = format_docs(docs)
        return context_store[session_id], docs, True  
    else:
        return context_store[session_id], None, False

store = {}
def session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    
    return store[session_id]

#Função para juntar o conteudo dos documentos obtidos na recuperação
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

os.environ["GOOGLE_API_KEY"] = gemini_key

# Difinição e configuração do llm , retriever , prompt e rag_chain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature = 0.7
    )

retriever = faiss_db.as_retriever(search_kwargs={"k": 2})

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em leis do consumidor,  Use o contexto."),
    MessagesPlaceholder("history"),
    ("user", "Contexto: {context} \n Pergunta: {question}")
])

rag_chain = (
    {
        "context": itemgetter("context"),
        "question": itemgetter("question"),
        "history": itemgetter("history"),
    }
    | prompt
    | llm
)

# Estabelencendo Conversação Robusta

chat_chain = RunnableWithMessageHistory(
    rag_chain,
    session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# Implementando Chat com RAG

while True:
    pergunta = input("prompt: ")

    if pergunta.lower() == "sair":
        print("Sessão Encerrada")
        break
    
    docs = retriever.invoke(pergunta)

    contexto, docs, primeira_vez = get_or_create_context("user_123", pergunta)

    resposta = chat_chain.invoke(
        {
            "question": pergunta,
            "context": contexto
        },
        config={"configurable": {"session_id": "user_123"}}
    )


    print(f"Reposta LLM : {resposta.content}")

    if primeira_vez:
        for i, doc in enumerate(docs) :
            print(f"[{i+1}]Documento recuperado:")
            print(f"Título: {doc.metadata.get('title')}")
            print(f"Fonte: {doc.metadata.get('source')}")
            print(f"Chunk ID: {doc.metadata.get('chunk_id')}")
            print("-" * 40)
            print(doc.page_content , "...\n")