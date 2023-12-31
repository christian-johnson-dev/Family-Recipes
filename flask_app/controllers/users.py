from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import user




@app.route("/")
def redirect_list():
    return redirect("/list")

@app.route("/login_reg")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not user.User.is_valid(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        id=user.User.create(data)
        session['user_id']=id
        session["first_name"] = data["first_name"]
        session["last_name"] = data["last_name"]
        session["email"] = data["email"]
        session["password"] = data["password"]
        session["logged_in"] = True

    return redirect("/list")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_from_db = user.User.get_by_email(data)

    if not user_from_db:
        flash("Invalid Login", 'login')
        return redirect(url_for("index"))
    if not bcrypt.check_password_hash(user_from_db.password, request.form["password"]):
        flash("Invalid login", 'login')
        return redirect(url_for("index"))

    
    session['user_id']=user_from_db.id
    session['email']=request.form['email']
    session['first_name']=user_from_db.first_name
    session['logged_in'] = True
    return redirect("/list")
    
@app.route("/success")
def success_display():
    if session.get('logged_in') == True:
        return render_template("wall.html")
    return "You are not logged in"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/list")