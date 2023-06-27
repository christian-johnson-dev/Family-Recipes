from flask_app import app
from flask import render_template, session, redirect,request
from flask_app.models.recipe import Recipe



@app.route("/list")
def recipes():
    return render_template("list.html",recipes = Recipe.get_all_recipes())

@app.route('/search_recipes', methods=["POST"])
def search_recipe():
    data = {
        'search' : '%'+request.form['search']+'%',
        'soundslike' : request.form['search']
    }
    recipes = Recipe.search(data)
    return render_template("list.html",recipes=recipes)

@app.route("/create_recipe")
def show_recipe_form():
    if session.get('logged_in') != True:
        return redirect("/login_reg")
    return render_template("create-recipe.html")

@app.route("/save_recipe", methods=['POST'])
def create_recipe():
    if session.get('logged_in') != True:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        return redirect("/create_recipe")
    Recipe.save(request.form)
    return redirect("/list")

@app.route('/one_recipe/<int:id>')
def show_recipe(id):
    # if session.get('logged_in') != True:
    #     return redirect("/login_reg")
    session['recipe_id']=id
    recipe = Recipe.get_one_recipe(id)
    
    return render_template("recipe.html",recipe=recipe)

# @app.route('/edit/<int:id>')
# def edit_title(id):
#     if session.get('logged_in') == True:
#         return redirect("/logout")
#     recipe = Recipe.get_one(id)
#     return render_template("",recipe=recipe)


@app.route('/edit_title', methods=['post'])
def edit_title():
    if session.get('logged_in') != True:
        return redirect("/logout")
    if not Recipe.validate_title(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_title(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_ingredients', methods=['post'])
def edit_ingredients():
    if session.get('logged_in') != True:
        return redirect("/logout")
    if not Recipe.validate_ingredients(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_ingredients(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_img', methods=['post'])
def edit_img():
    if session.get('logged_in') != True:
        return redirect("/logout")
    
    Recipe.change_img(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_description', methods=['post'])
def edit_description():
    if session.get('logged_in') != True:
        return redirect("/logout")
    if not Recipe.validate_description(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_description(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/edit_directions', methods=['post'])
def edit_directions():
    if session.get('logged_in') != True:
        return redirect("/logout")
    if not Recipe.validate_directions(request.form):
        print(request.form)

        return redirect(f"/one_recipe/{request.form['id']}")
    Recipe.change_directions(request.form)
    return redirect(f"/one_recipe/{request.form['id']}")

@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    if session.get('logged_in') != True:
        return redirect("/login_reg")
    Recipe.delete(id)
    return redirect ("/list")



