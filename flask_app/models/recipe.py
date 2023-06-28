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
        self.directions = data['directions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted_by=None
        self.comments=[]

    @classmethod
    def save (cls, data):
        query = """INSERT INTO recipes (title,ingredients,img,description,directions,user_id)
                VALUES (%(title)s,%(ingredients)s,%(img)s,%(description)s,%(directions)s,%(user_id)s);"""
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
    
    @classmethod
    def search(cls, data):
        
        query = """
                SELECT * FROM recipes
                LEFT JOIN users ON users.id=recipes.user_id 
                WHERE title LIKE %(search)s OR
                title SOUNDS LIKE %(soundslike)s;
                """
        results=connectToMySQL(cls.db).query_db(query,data)
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

    @classmethod
    def get_users_recipes(cls, id):
        
        query = """
                SELECT * FROM recipes
                LEFT JOIN users ON users.id=recipes.user_id
                WHERE user_id = %(id)s;
                """
        results=connectToMySQL(cls.db).query_db(query,{'id':id})
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
            flash("Title must be at least 3 characters!","title")
            is_valid = False
        if len(recipe['ingredients'])<3:
            flash("Ingredients  must be at least 3 characters!","ingredients")
            is_valid = False
        if len(recipe['description'])<3:
            flash("Description  must be at least 3 characters!","description")
            is_valid = False
        
        return is_valid

    

    @staticmethod
    def validate_title(recipe):
    
        is_valid = True
        if len(recipe['title'])<3:
            flash("Title must be at least 3 characters!","title")
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_ingredients(recipe):
    
        is_valid = True
        
        if len(recipe['ingredients'])<3:
            flash("Ingredients  must be at least 3 characters!","ingredients")
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_description(recipe):
    
        is_valid = True
        
        if len(recipe['description'])<3:
            flash("Description  must be at least 3 characters!","description")
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_directions(recipe):
    
        is_valid = True
        
        if len(recipe['directions'])<3:
            flash("Directions must be at least 3 characters!","directions")
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
                'id' : recipe['users.id'],
                'first_name':recipe['first_name'],
                'last_name':recipe['last_name'],
                'email':recipe['email'],
                'password':recipe['password'],
                'created_at':recipe['users.created_at'],
                'updated_at':recipe['users.updated_at']
                }
        recipe = cls(recipe)        
        recipe.posted_by=User(user_info)
        recipe.comments = Comment.get_recipes_comments(id)
        print()
        print("Recipe:" + recipe.img)
        print()

        return recipe

    @classmethod
    def get_recipes_comments(cls, id):
        
        query = """SELECT * FROM comments
                    LEFT JOIN recipes ON comments.recipe_id=recipes.id
                    WHERE recipes.id = %(id)s;"""
        
        results = connectToMySQL(cls.db).query_db(query,{"id":id})
        comments = []
        print("This is the result")
        print(results)
        for result in results:
            comment = Comment(result)
            comments.append( comment )
            # user_info = {
            #     'id' : result['id'],
            #     'text':result['text'],
            #     'user_id':result['user_id'],
            #     'recipe_id':result['recipe_id'],
            #     'created_at':result['users.created_at'],
            #     'updated_at':result['users.updated_at']
            #     }
            # comment.posted_by=User(user_info)
            # comments = comments
        return comments

    @classmethod
    def change_title(cls,data):
        query="""UPDATE recipes SET title=%(title)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def change_ingredients(cls,data):
        query="""UPDATE recipes SET ingredients=%(ingredients)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def change_img(cls,data):
        query="""UPDATE recipes SET img=%(img)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def change_description(cls,data):
        query="""UPDATE recipes SET description=%(description)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def change_directions(cls,data):
        query="""UPDATE recipes SET directions=%(directions)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes  WHERE recipes.id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        return result