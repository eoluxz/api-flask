from flask import Flask, jsonify

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "Beatriz"},
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Alunos - Acesse /alunos"})

@app.route("/", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

if __name__ == "__main__":
    app.run(port=5001)