import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

def ask_veyra(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']

# Test command
if __name__ == "__main__":
    prompt = input("Veyra > ")
    reply = ask_veyra(prompt)
    print(f"🤖: {reply}")
