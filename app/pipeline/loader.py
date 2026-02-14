from app.core.logger import logger
import glob
import os

def load_pdfs(directory: str) -> list[str]:
    try:
        return glob.glob(os.path.join(directory, "*.pdf"))
    
    except Exception:
        logger.exception(f"ERROR loader.py (load_pdfs)")
        raise