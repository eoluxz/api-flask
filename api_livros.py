from flask import Flask, jsonify

app = Flask(__name__)

Livros = [
    {"id": 1, "nome": "Star Wars: A vingança dos sith"},
    {"id": 2, "nome": "Vivendo uma vida autentica"},
    {"id": 3, "nome": "O principe"},
]

@app.route("/livros", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Livros - Acesse /livros"})

@app.route("/", methods=["GET"])
def listar_livros():
    return jsonify(__name__)

if __name__ == "_main_":
    app.run(port=5001)