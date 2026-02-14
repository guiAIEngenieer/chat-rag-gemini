from app.utils.validation import validate_prompt

def test_validate_prompt():
    assert validate_prompt("") is not None
    assert validate_prompt("ok") is not None
    assert validate_prompt("a" * 1001) is not None
    assert validate_prompt("pergunta valida") is None

