import os
from dotenv import load_dotenv
from app.core.logger import logger

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PDF_DIRECTORY = os.getenv("PDF_DIRECTORY")

if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY not configured")

if not PDF_DIRECTORY:
    logger.error("PDF_DIRECTORY not configured")