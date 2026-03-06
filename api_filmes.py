from flask import Flask, jsonify

app = Flask(__name__)

Filmes = [
    {"id": 1, "nome": "Jogador numero 1"},
    {"id": 2, "nome": "Vingadores: Ultimato"},
    {"id": 3, "nome": "Operação Big Hero"},
]

@app.route("/filmes", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Filmes - Acesse /filmes"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(__name__)

if __name__ == "_main_":
    app.run(port=5001)