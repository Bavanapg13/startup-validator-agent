import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set. Please check your .env file.")
    
MODEL_NAME = "llama-3.1-8b-instant"
