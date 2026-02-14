from langchain_community.chat_message_histories import ChatMessageHistory

class SessionManager:
    def __init__(self):
        self.store = {}

    def get_context(self, question, retriever):
        docs = retriever.invoke(question)
        return self._format_docs(docs)

    def session_history(self, session_id):
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    @staticmethod
    def _format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

manager = SessionManager()