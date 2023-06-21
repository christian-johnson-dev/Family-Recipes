from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.comment import Comment

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
        self.user_id = data['users_id']
        self.posted_by=None
        self.comments=[]

    @classmethod
    def save (cls, data):
        query = """INSERT INTO recipes (title,ingredients,img,description,user_id)
                VALUES (%(title)s,%(ingredients)s,%(img)s,%(description)s,%(user_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM recipes
                    LEFT JOIN users ON users.id=recipes.user_id;"""
        
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        
        for result in results:
            recipe = cls(result)
            recipes.append( recipe )
            user_info = {
                'id' : result['users.id'],
                'first_name':result['first_name'],
                'last_name':result['last_name'],
                'email':result['email'],
                'password':result['password'],
                'created_at':result['users.created_at'],
                'updated_at':result['users.updated_at']
                }
            recipe.posted_by=User(user_info)
            
        return recipes

    @staticmethod
    def validate_recipe(recipe):
    
        is_valid = True
        if len(recipe['title'])<3:
            flash("Title must be at least 3 characters!")
            is_valid = False
        if len(recipe['ingredients'])<3:
            flash("Ingredients  must be at least 3 characters!")
            is_valid = False
        if len(recipe['description'])<3:
            flash("Description  must be at least 3 characters!")
            is_valid = False
        
        return is_valid

    @classmethod
    def get_one_recipe(cls, id):
        query = """SELECT * FROM recipes 
        LEFT JOIN users ON users.id=recipes.user_id
        WHERE recipes.id= %(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        recipe = result[0]
        user_info = {
                'id' : result['users.id'],
                'first_name':result['first_name'],
                'last_name':result['last_name'],
                'email':result['email'],
                'password':result['password'],
                'created_at':result['users.created_at'],
                'updated_at':result['users.updated_at']
                }
        recipe.posted_by=User(user_info)
        recipe.comments=Comment.get_comments_by_recipe_id(id)
        return recipe

    @classmethod
    def change(cls,data):
        query="""UPDATE recipes SET title=%(title)s, ingredients=%(ingredients)s,img=%(img)s,
                description=%(description)s,user_id=%(user_id)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes  WHERE recipes.id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        return result 


