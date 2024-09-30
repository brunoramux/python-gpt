import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-WrBbPUYsyf8MVSfE9AFENHBN"

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.Model.list())