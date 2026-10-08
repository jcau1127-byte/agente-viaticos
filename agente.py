import os

from dotenv import load_dotenv
from google import genai

MODELO = "gemini-3.5-flash-lite"
INSTRUCCIONES = "Responde siempre en español y en máximo 3 frases."

load_dotenv()
cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def responder(pregunta: str) -> str:
    interaccion = cliente.interactions.create(
        model=MODELO,
        input=pregunta,
        system_instruction=INSTRUCCIONES,
    )
    return interaccion.output_text


if __name__ == "__main__":
    while True:
        pregunta = input("Tú (vacío para salir): ").strip()
        if not pregunta:
            break
        print(f"Agente: {responder(pregunta)}\n")
