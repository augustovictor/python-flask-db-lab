import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, Api, reqparse
from models.item import Item

class ItemApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank!')

    # @jwt_required()
    def get(self, name):
        item = Item.findByName(name)
        if item:
            return item.json()
        return { 'message': 'Item not found' }, 404

    def post(self, name):
        if Item.findByName(name):
            return { 'message': 'Item with given name already exists'}, 400

        data = ItemApi.parser.parse_args()
        item = Item(None, data['name'], data['price'])

        try:
            item.save_to_db()
            return item.json(), 201
        except:
            return { 'message': 'Something went wrong while creating the item' }, 500


    def delete(self, name):
        pass

    def put(self, name):
        pass
