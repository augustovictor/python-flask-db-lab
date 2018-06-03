from flask_restful import Resource, Api, reqparse
from models.store import Store

class StoreResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank!')

    def get(self, name):
        # data = StoreResource.parser.parse_args()
        store = Store.find_by_name(name)

        if store:
            print('WE GOT STORE')
            return store.json()
        
            
        return ({ 'message': 'No store found for given name'}, 404)

    def post(self, name):
        # data = StoreResource.parser.parse_args()

        if Store.find_by_name(name):
            return { 'message': 'Store name already taken' }, 400

        store = Store(name)

        try:
            store.save_to_db()
            return store.json(), 200
        except:
            return { 'message': 'Something went wrong while creating the store.' }, 500