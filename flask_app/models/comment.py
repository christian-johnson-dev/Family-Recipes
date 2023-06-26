from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Comment:
    db = "family_recipes"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posted_by = None

    # Create a comment given data from request form
    @classmethod
    def save (cls, data):
        query = """INSERT INTO comments (text,user_id,recipe_id)
                VALUES (%(text)s,%(user_id)s,%(recipe_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    # Edit a comment given data from request form
    @classmethod
    def change(cls,data):
        query="""UPDATE recipes SET title=%(title)s, ingredients=%(ingredients)s,img=%(img)s,
                description=%(description)s,user_id=%(user_id)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    # Given a comment id this will delete comment
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM comments WHERE comments.id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        return result

    # Given a recipe id this will return all comments
    @classmethod
    def get_recipes_comments(cls, id):
        # query = """SELECT * FROM comments
        #             LEFT JOIN recipes ON comments.recipe_id=recipes.id
        #             LEFT JOIN users ON recipes.user_id=users.id 
        #             WHERE comments.user_id = %(id)s;"""
        
        query = """
                SELECT * FROM comments
                JOIN users on comments.user_id=users.id
                WHERE comments.recipe_id = %(id)s
                ORDER BY comments.created_at DESC;
                """

        results = connectToMySQL(cls.db).query_db(query,{"id":id})
        comments = []
        for result in results:
            comment = cls(result)
            comments.append( comment )
            user_info = {
                'id' : result['users.id'],
                'first_name':result['first_name'],
                'last_name':result['last_name'],
                'email':result['email'],
                'password':result['password'],
                'created_at':result['users.created_at'],
                'updated_at':result['users.updated_at']
                }
            comment.posted_by=User(user_info)
        return comments

    # Do you need to get one comment?

    # @classmethod
    # def get_one_comment(cls, id):
    #     query = """SELECT * FROM comments 
    #     LEFT JOIN recipe ON comments.recipe_id=recipes.id
    #     WHERE comment.id= %(id)s;"""
    #     result=connectToMySQL(cls.db).query_db(query,{'id':id})
    #     comment = result[0]
    #     user_info = {
    #             'id' : result['users.id'],
    #             'first_name':result['first_name'],
    #             'last_name':result['last_name'],
    #             'email':result['email'],
    #             'password':result['password'],
    #             'created_at':result['users.created_at'],
    #             'updated_at':result['users.updated_at']
    #             }
    #     comment.posted_by=User(user_info)
    #     comment.comments=Comment.get_comments_by_recipe_id(id)
    #     return recipe

    

    @staticmethod
    def validate_comment(comment):
    
        is_valid = True
        if len(comment['text'])<3:
            flash("Title must be at least 3 characters!")
            is_valid = False
        
        return is_valid