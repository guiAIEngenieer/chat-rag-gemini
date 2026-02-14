from app.pipeline.loader import load_pdfs

def test_load_pdfs(tmp_path):
    (tmp_path / "doc1.pdf").touch()
    (tmp_path / "doc2.pdf").touch()
    (tmp_path / "outro.txt").touch()

    pdfs = load_pdfs(tmp_path)

    assert len(pdfs) == 2
