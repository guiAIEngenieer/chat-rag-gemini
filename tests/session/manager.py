from app.session.manager import SessionManager

class FakeRetriever:
    def invoke(self, question):
        class Doc:
            page_content = "conteudo"
        return [Doc()]

def test_get_or_create_context():
    manager = SessionManager()
    retriever = FakeRetriever()

    context, docs, first = manager.get_or_create_context(
        "chat1", "pergunta", retriever
    )

    assert first is True
    assert "conteudo" in context
