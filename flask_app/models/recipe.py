from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    db = "family_recipes"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.ingredients = data['ingredients']
        self.img = data['img']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']