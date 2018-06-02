import sqlite3
from flask_restful import Resource, Api, reqparse
from  models.user import User

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank!')
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return { 'message': 'Username already taken!'}, 400

        # user = User(1, data['username'], data['password'])
        # createdUser = User.signup(data['username'], data['password'])
        # return createdUser, 201 if createdUser else None, 400

        User.signup(data['username'], data['password'])

        return { 'message': 'User created successfully!' }, 201