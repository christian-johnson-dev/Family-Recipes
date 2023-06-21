from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    db = "family_recipes"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):