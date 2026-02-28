from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ✅ CREATE FASTAPI APP FIRST
app = FastAPI()

# ✅ Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ✅ CHAT ROUTE
@app.get("/chat")
def chat(question: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}]
        )

        reply = response.choices[0].message.content
        return {"answer": reply}

    except Exception as e:
        return {"answer": str(e)}

# ✅ SERVE FRONTEND (KEEP LAST)
app.mount("/", StaticFiles(directory="static", html=True), name="static")