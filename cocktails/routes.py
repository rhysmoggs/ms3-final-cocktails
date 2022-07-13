from flask import (
    flash, render_template,
    request, redirect, session, url_for)
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from cocktails import app, db, mongo
from cocktails.models import Category, Users


@app.route("/")
@app.route("/home")
def home():
    categories = list(Category.query.order_by(Category.category_name).all())
    cocktails = list(mongo.db.cocktails.find())
    return render_template("home.html", categories=categories, cocktails=cocktails)


# @app.route("/all_cocktails")
# def all_cocktails():
#     cocktails = list(mongo.db.cocktails.find())
#     return render_template("all_cocktails.html", cocktails=cocktails)


@app.route("/all_cocktails")
def all_cocktails():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # maximum amount of cocktails to be displayed per page
    per_page = 9
    offset = (page - 1) * per_page
    cocktails = list(mongo.db.cocktails.find())
    # the total amount of cocktails found in the mongo cocktails collection
    total = len(cocktails)
    cocktails_paginated = cocktails[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template("all_cocktails.html",
                           cocktails=cocktails_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/filter_category/<int:category_id>")
def filter_category(category_id):

    # category = Category.query.get_or_404(category_id)
    cocktails = list(mongo.db.cocktails.find({"category_id": str(category_id)}))
    return render_template("filter_category.html", cocktails=cocktails)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cocktails = list(mongo.db.cocktails.find({"$text": {"$search": query}}))
    return render_template("all_cocktails.html", cocktails=cocktails)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # create a dictionary
        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                # better for brute forcing by not hinting which is incorrect.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if "user" in session:
        cocktails = list(mongo.db.cocktails.find())
        return render_template("profile.html", username=session["user"], cocktails=cocktails)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_categories")
def get_categories():

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage cocktail categories!")
        return redirect(url_for("all_cocktails"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage ccktail categories!")
        return redirect(url_for("all_cocktails"))

    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        flash("New Cocktail Category Added")
        return redirect(url_for("get_categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("all_cocktails"))

    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        flash("Cocktail Category Updated")
        return redirect(url_for("get_categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    if session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("all_cocktails"))

    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    mongo.db.cocktails.delete_many({"category_id": str(category_id)})
    flash("Cocktail Category Deleted")
    return redirect(url_for("get_categories"))


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if "user" not in session:
        flash("You need to be logged in to add a cocktail")
        return redirect(url_for("all_cocktails"))

    if request.method == "POST":
        cocktail = {
            "category_id": request.form.get("category_id"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_description": request.form.get("cocktail_description"),
            "main_ingredient": request.form.get("main_ingredient"),
            "created_by": session["user"],
            "method": request.form.getlist("method"),
            "other_ingredient": request.form.getlist("other_ingredient"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings")
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Cocktail Successfully Added")
        return redirect(url_for("all_cocktails"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add_cocktail.html", categories=categories)


@app.route("/view_cocktail/<cocktail_id>")
def view_cocktail(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    return render_template("view_cocktail.html", cocktail=cocktail)


@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    if "user" not in session or session["user"] != cocktail["created_by"]:
        flash("You can only edit your own cocktails!")
        return redirect(url_for("all_cocktails"))

    if request.method == "POST":
        submit = {
            "category_id": request.form.get("category_id"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_description": request.form.get("cocktail_description"),
            "main_ingredient": request.form.get("main_ingredient"),
            "created_by": session["user"],
            "method": request.form.getlist("method"),
            "other_ingredient": request.form.getlist("other_ingredient"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings")
        }
        mongo.db.cocktails.update_one({"_id": ObjectId(cocktail_id)}, {"$set": submit})
        flash("Cocktail Successfully Updated")
        return redirect(url_for("all_cocktails"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("edit_cocktail.html", cocktail=cocktail, categories=categories)


@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    if "user" not in session or session["user"] != cocktail["created_by"]:
        flash("You can only delete your own cocktails!")
        return redirect(url_for("all_cocktails"))

    mongo.db.cocktails.delete_one({"_id": ObjectId(cocktail_id)})
    flash("Cocktail Successfully Deleted")
    return redirect(url_for("all_cocktails"))
