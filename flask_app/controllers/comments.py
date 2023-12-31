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
    return redirect(f"/one_recipe/{recipe_id}")

@app.route("/delete_comment/<recipe_id>/<id>")
def delete_comment(id,recipe_id):
    comment.Comment.delete(id)
    return redirect(f"/one_recipe/{recipe_id}")

@app.route("/edit_comment/<recipe_id>/<comment_id>", methods=["POST"])
def edit_comment(recipe_id, comment_id):
    current_comment = comment.Comment.get_comment_user(comment_id)
    if current_comment.user_id != session["user_id"]:
        print("not logged_in")
        return redirect(f"/one_recipe/{recipe_id}")
    print(session)
    print("CURRENT USER ID:")
    print("CURRENT USER ID:")
    print("CURRENT USER ID:")
    print("CURRENT USER ID:")
    print("CURRENT USER ID:")
    print(current_comment.user_id)
    data = {
        'id':comment_id,
        'text':request.form['comment-update']
    }
    comment.Comment.change(data)
    return redirect(f"/one_recipe/{recipe_id}")