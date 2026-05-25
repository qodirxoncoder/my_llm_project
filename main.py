from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = []

while True:
    user_input = input("Sen: ")
    if user_input == "exit":
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    
    print(f"AI: {answer}\n")