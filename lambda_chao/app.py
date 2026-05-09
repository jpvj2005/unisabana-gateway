from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handler():
    body = request.get_json() or {}
    mensaje = body.get("mensaje", "")
    return jsonify({
        "statusCode": 200,
        "origen": "Lambda 2 - Unisabana",
        "respuesta": f"Hasta luego! Recibi tu mensaje: '{mensaje}'"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
