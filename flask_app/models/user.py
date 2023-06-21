from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "family_recipes"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """INSERT INTO users (first_name, last_name, email, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * from users where email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return False

    
    @staticmethod
    def is_valid(user_dict):
        is_valid = True
        if len(user_dict["first_name"]) < 2:
            is_valid = False
            flash("First name should have at least 2 characters", "registration")
        if len(user_dict["last_name"]) < 2:
            is_valid = False
            flash("Last name should have at least 2 characters", "registration")
        if len(user_dict["email"]) < 2:
            is_valid = False
            flash("Email should have at least 2 characters", "registration")
        if len(user_dict["password"]) < 2:
            is_valid = False
            flash("Password should have at least 2 characters", "registration")
        if user_dict["password_confirmation"] != user_dict["password"]:
            is_valid = False
            flash("Password must match password confirmation", "registration")
        return is_valid
    
    @staticmethod
    def valid_login(user_dict):
        is_valid = True
        if len(user_dict["email"]) < 2:
            is_valid = False
            flash("Email should have at least 2 characters")
        if len(user_dict["password"]) < 2:
            is_valid = False
            flash("Password should have at least 2 characters")
        # if user_dict["password_confirmation"] != user_dict["password"]:
        #     is_valid = False
        #     flash("Password must match password confirmation")
        return is_valid 