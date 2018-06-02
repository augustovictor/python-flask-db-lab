import sqlite3
from db import db

class Item(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    def json(self):
        return { 'name:': self.name, 'price': self.price }
    
    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items WHERE id = ?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        item = cls(*row) if row else None
        connection.close()
        return item

    @classmethod
    def findByName(cls, name):
        return Item.query.filter_by(name=name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()