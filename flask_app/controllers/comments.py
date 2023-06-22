from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import comment

@app.route("/display_create_comment")
def display_create_comment():
    if session.get('logged_in') == True:
        return render_template("")
    else:
        return redirect("/")

@app.route("/create_comment/<recipe_id>")
def create_comment(recipe_id):
    data = request.form
    comment.Comment.save(data)
    return redirect()

@app.route("delete_comment/<id>")
def delete_comment(id):
    comment.Comment.delete(id)
    return redirect()

@app.route("edit_comment/<id>")
def edit_comment(id):
    comment.Comment.edit()