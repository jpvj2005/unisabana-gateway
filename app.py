from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SALUDOS = {"hola"}
DESPEDIDAS = {"chao", "adios", "adios"}

def lambda_hola(mensaje):
    return {
        "statusCode": 200,
        "origen": "Lambda 1 - Unisabana",
        "respuesta": f"Hola! Recibi tu mensaje: '{mensaje}'"
    }

def lambda_chao(mensaje):
    return {
        "statusCode": 200,
        "origen": "Lambda 2 - Unisabana",
        "respuesta": f"Hasta luego! Recibi tu mensaje: '{mensaje}'"
    }

@app.route("/mensaje", methods=["POST"])
def gateway():
    body = request.get_json() or {}
    mensaje = body.get("mensaje", "").strip().lower()

    if mensaje in SALUDOS:
        result = lambda_hola(mensaje)
    elif mensaje in DESPEDIDAS:
        result = lambda_chao(mensaje)
    else:
        result = {
            "statusCode": 200,
            "origen": "Gateway - Unisabana",
            "respuesta": f"Mensaje '{mensaje}' no reconocido."
        }

    return jsonify(result), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
