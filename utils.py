import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_serper_api_key():
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key


