from flask import Flask, jsonify
from flask import Blueprint

loja_blueprint = Blueprint('loja', __name__)
pedido_blueprint = Blueprint('pedido', __name__)
produto_blueprint = Blueprint('produto', __name__)
perfil_blueprint = Blueprint('perfil', __name__)

@loja_blueprint.route('/')
def loja():
    return jsonify({"message": "Página da Loja"})

@pedido_blueprint.route('/')
def pedido():
    return jsonify({"message": "Página de Pedidos"})

@produto_blueprint.route('/')
def produto():
    return jsonify({"message": "Página de Produtos"})

@perfil_blueprint.route('/')
def perfil():
    return jsonify({"message": "Página de Perfil"})

app = Flask(__name__)

app.config['DEBUG'] = True 

app.register_blueprint(loja_blueprint, url_prefix='/loja')
app.register_blueprint(pedido_blueprint, url_prefix='/pedido')
app.register_blueprint(produto_blueprint, url_prefix='/produto')
app.register_blueprint(perfil_blueprint, url_prefix='/perfil')

@app.route('/')
def home():
    return jsonify({"message": "Bem vindo à API do e-commerce!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)