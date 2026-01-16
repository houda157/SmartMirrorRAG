import requests
import json
import llm
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

openai_key = os.getenv("API_KEY")
openai_url = os.getenv("API_URL")

print("API_KEY loaded:", bool(openai_key))
print("API_URL loaded:", openai_url)

query="what are the events related to AI?"

context = llm.get_context(
    query="what are the events related to AI?"
)

print("Context Retrieved:\n", context)

headers = {
    "Authorization": f"Bearer {openai_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Context Query Example"
}

data = {
    "model": "tngtech/deepseek-r1t2-chimera:free",
    "messages": [
        {
            "role": "system",
            "content": "Answer ONLY using the provided context."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{query}"
        }
    ],
    "temperature": 0.2
}

response = requests.post(openai_url, headers=headers, data=json.dumps(data))
result = response.json()
print("result:")
print(result["choices"][0]["message"]["content"])
