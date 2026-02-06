import os
from dotenv import load_dotenv

load_dotenv("chaves.env")
gemini_key = os.getenv("GEMINI_API_KEY")
