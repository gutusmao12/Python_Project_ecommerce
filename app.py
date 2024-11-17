from flask import Flask, jsonify
from flask import Blueprint

loja_blueprint = Blueprint('loja', __name__)

@loja_blueprint.route('/')
def index():
    return "Página inicial da loja"

app = Flask(__name__)

app.config['DEBUG'] = True 

app.register_blueprint(loja_blueprint)

@app.route('/')
def home():
    return jsonify({"message": "Bem vindo à API do e-commerce!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)