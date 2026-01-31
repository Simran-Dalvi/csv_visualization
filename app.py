import os
from dotenv import load_dotenv

load_dotenv()

print ("API key loaded :", os.getenv("OPENAI_API_KEY") is not None)