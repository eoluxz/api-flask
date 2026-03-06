from flask import Flask, jsonify

app = Flask(__name__)

Jogos = [
    {"id": 1, "nome": "Just Dance"},
    {"id": 2, "nome": "Valorant"},
    {"id": 3, "nome": "Fortnite"},
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(__name__)

if __name__ == "_main_":
    app.run(port=5001)