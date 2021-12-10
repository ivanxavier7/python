from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Creane new endpoit /auth, send user and password with authenticate, if match uses de JWT token in identity to search the user that is token represents

api.add_resource(Item, '/item/<string:name>') # https://127.0.0.1:5000/item/Exemplo
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # debug=True para desenvolver
