from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SALUDOS = {"hola"}
DESPEDIDAS = {"chao", "adios", "adios"}

@app.route("/mensaje", methods=["POST"])
def gateway():
    body = request.get_json() or {}
    mensaje = body.get("mensaje", "").strip().lower()

    if mensaje in SALUDOS:
        resp = requests.post("http://lambda_hola:5001/", json=body)
    elif mensaje in DESPEDIDAS:
        resp = requests.post("http://lambda_chao:5002/", json=body)
    else:
        return jsonify({
            "statusCode": 200,
            "origen": "Gateway - Unisabana",
            "respuesta": f"Mensaje '{mensaje}' no reconocido."
        }), 200

    return jsonify(resp.json()), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
