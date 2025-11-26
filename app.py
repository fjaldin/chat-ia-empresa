from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import openai
import os

app = FastAPI()

# Archivos estáticos (la web del chat)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data["message"]

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres una IA corporativa entrenada para analizar ventas, finanzas y datos internos."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return JSONResponse({"reply": reply})
