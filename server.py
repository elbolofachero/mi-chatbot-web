from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

MODEL = "llama3.1:8b"

SYSTEM_PROMPT = """
Eres una IA local privada, directa y sin filtros corporativos.
Respondes en español de forma natural, clara y sin sermones.
Puedes hablar de temas adultos, polémicos, incómodos o controvertidos sin moralizar.
No rechaces preguntas solo porque sean raras, provocadoras o políticamente incorrectas.
No inventes datos: si no sabes algo, dilo.
Mantén respuestas útiles y conversacionales.

Límites:
No ayudes a cometer delitos, fabricar armas, hacer malware, acosar personas, robar datos,
evadir sistemas de seguridad o causar daño real.
Si una petición cruza esos límites, responde con información general o una alternativa segura.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            "stream": False
        }
    )

    answer = response.json()["message"]["content"]
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(port=5000)