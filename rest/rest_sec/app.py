from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from user import UserRegister

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Creane new endpoit /auth, send user and password with authenticate, if match uses de JWT token in identity to search the user that is token represents

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
        )   # Just accept price, other arguments will be ignored
    
    @jwt_required()   # Decorator that require de authentication before "get"
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)     # Search for the first 'name' inside items, if not find retreive None
        return {'item': item}, 200 if item else 404      # SUCCESS or NOT FOUND
    
    def post(self, name):
        
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400  # BAD REQUEST
        data = Item.parser.parse_args()
        item = {
            'name': name,
            'price': data['price']
            }
        items.append(item)
        return item, 201                # CREATED
    
    def delete(self, name):
        global items    # To use items variable out of class
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted.'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            item.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>') # https://127.0.0.1:5000/item/Exemplo
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


app.run(port=5000, debug=True)  # debug=True para desenvolver
