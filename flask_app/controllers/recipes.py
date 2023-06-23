from flask_app import app
from flask import render_template, session, redirect,request
from flask_app.models.recipe import Recipe


@app.route("/list")
def recipes():
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("list.html",recipes = Recipe.get_all_recipes())

@app.route("/create_recipe")
def show_recipe_form():
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("create-recipe.html")

@app.route("/save_recipe", methods=['post'])
def create_recipe():
    print(request.form)
    if 'user_id' not in session:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        return redirect("/create_recipe")
    Recipe.save(request.form)
    return redirect("/list")

@app.route('/one_recipe/<int:id>')
def show_recipe(id):
    if session.get('logged_in') == True:
        return redirect("/logout")
    session['recipe_id']=id
    recipe = Recipe.get_one(id)
    
    return render_template("recipe.html",recipe=recipe)

# @app.route('/edit/<int:id>')
# def edit_title(id):
#     if session.get('logged_in') == True:
#         return redirect("/logout")
#     recipe = Recipe.get_one(id)
#     return render_template("",recipe=recipe)


@app.route('/edit_title', methods=['post'])
def edit_title():
    if session.get('logged_in') == True:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_title(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_ingredients', methods=['post'])
def edit_ingredients():
    if session.get('logged_in') == True:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_ingredients(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_img', methods=['post'])
def edit_img():
    if session.get('logged_in') == True:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_img(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_description', methods=['post'])
def edit_description():
    if session.get('logged_in') == True:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_description(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if session.get('logged_in') == True:
        return redirect("/logout")
    Recipe.delete(id)
    return redirect ("/recipes")





