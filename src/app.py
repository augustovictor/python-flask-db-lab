from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from resources.user import UserRegister
from models.user import User
from resources.item import ItemApi
from models.item import Item
from resources.item import ItemList
from resources.store import StoreResource

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.secret_key = '/x12;3117529110^%@!'

jwt = JWT(app, authenticate, identity) # /auth

items = []

api.add_resource(ItemApi, '/items/<string:name>')
api.add_resource(UserRegister, '/users')
api.add_resource(ItemList, '/item-list')
api.add_resource(StoreResource, '/stores/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=3000, debug=True)