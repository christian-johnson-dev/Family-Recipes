from flask_app import app
from flask import render_template, session, flash, redirect,request,send_from_directory,url_for
from flask_app.models.recipe import Recipe
from werkzeug.utils import secure_filename
import os



ALLOWED_EXTENSIONS={'png','jpg','jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



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
    print(recipes)
    if(recipes==[]):
        flash('No results found')
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
    
    filename="" #default 
    
    img = request.files['img']
        # if user does not select file, browser also
        # submit an empty part without filename
    if img and img.filename!='':
        if allowed_file(img.filename): 
       
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            

    new_recipe={
        'title':request.form['title'],
        'ingredients':request.form['ingredients'],
        'img':filename,
        'description':request.form['description'],
        'directions':request.form['directions'],
        'user_id':request.form['user_id']
        }
            
    Recipe.save(new_recipe)
    return redirect("/list")


@app.route('/one_recipe/<int:id>')
def show_recipe(id):
    
    session['recipe_id']=id
    recipe = Recipe.get_one_recipe(id)
    print(recipe.img)
    
    
    return render_template("recipe.html",recipe=recipe)

#get all of the recipe of user with user_id = id
@app.route('/user_recipes/<id>')
def users_recipes(id):
    recipes = Recipe.get_users_recipes(id)
    return render_template("list.html",recipes=recipes) 

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



