#importing libraries
import requests
import json
from config import OPENROUTER_API_KEY


#using LLama Model
LLAMA_MODEL = "meta-llama/llama-4-maverick:free"
OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"


#writing function for generate response
def generate_llm_response(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Voice-AI-Demo"
    }

    payload = {
        "model": LLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful but concise voice assistant. Answer the user query clearly and briefly ."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(
            url=OPENROUTER_ENDPOINT,
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.RequestException as e:
        return f"Error communicating with LLaMA-4: {e}"
    except KeyError:
        return "Unexpected LLaMA response format."