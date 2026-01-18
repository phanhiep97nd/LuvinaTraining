import os
import sys
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def ask_gemini(prompt: str):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if len(sys.argv) > 1:
    question = " ".join(sys.argv[1:])
    print(ask_gemini(question))
else:
    print("🤖 Gemini CLI (exit để thoát)\n")
    while True:
        q = input("Bạn: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("\nGemini:")
        print(ask_gemini(q))
        print("-" * 40)
