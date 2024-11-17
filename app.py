from flask import Flask, jsonify
from loja import loja_blueprint

app = Flask(__name__)

app.config['DEBUG'] = True 

app.register_blueprint(loja_blueprint)

@app.route('/')
def home():
    return jsonify({"message": "Bem vindo à API do e-commerce!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)