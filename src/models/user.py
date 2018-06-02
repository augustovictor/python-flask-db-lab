import sqlite3
from db import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        select_query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        
        user = cls(*row) if row else None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = 'SELECT * FROM users WHERE id = ?'
        result = cursor.execute(select_query, (_id,))
        row = result.fetchone()

        user = cls(*row) if row else None

        connection.close()
        return user

    @classmethod
    def signup(cls, username, password):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_user_query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        # user = cls(None, username, password)
        result = cursor.execute(create_user_query, (username, password))
        # user = result.fetchone()
        connection.commit()
        connection.close()
        return True