from flask import Flask, jsonify, Blueprint, render_template
import os

loja_blueprint = Blueprint('loja', __name__)
pedido_blueprint = Blueprint('pedido', __name__)
produto_blueprint = Blueprint('produto', __name__)
perfil_blueprint = Blueprint('perfil', __name__)

@loja_blueprint.route('/')
def loja():
     return render_template('loja.html')

@pedido_blueprint.route('/')
def pedido():
     return render_template('pedido.html')

@produto_blueprint.route('/')
def produto():
     return render_template('produto.html')

@perfil_blueprint.route('/')
def perfil():
     return render_template('perfil.html')

app = Flask(__name__)

app.config['DEBUG'] = False 

app.register_blueprint(loja_blueprint, url_prefix='/loja')
app.register_blueprint(pedido_blueprint, url_prefix='/pedido')
app.register_blueprint(produto_blueprint, url_prefix='/produto')
app.register_blueprint(perfil_blueprint, url_prefix='/perfil')

@app.route('/')
def home():
    return jsonify({"message": "Bem vindo à API do e-commerce!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)