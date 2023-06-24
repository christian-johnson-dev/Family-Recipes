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

@app.route("/create_comment/<recipe_id>", methods=["POST"])
def create_comment(recipe_id):
    data = request.form
    comment.Comment.save(data)
    return redirect()

@app.route("/delete_comment/<recipe_id>/<id>")
def delete_comment(id,recipe_id):
    comment.Comment.delete(id)
    return redirect(f"/one_recipe/{recipe_id}")

@app.route("/edit_comment/<id>", methods=["POST"])
def edit_comment(id):
    comment.Comment.edit()
    return redirect("")