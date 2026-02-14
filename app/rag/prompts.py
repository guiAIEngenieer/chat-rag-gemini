from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

RAG_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "Use o contexto para responder a pergunta. Utilize apenas o documento mais relevante."),
    MessagesPlaceholder("history"),
    ("user", "Contexto: {context}\nPergunta: {question}")
])
