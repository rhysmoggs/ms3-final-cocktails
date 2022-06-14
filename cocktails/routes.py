from flask import (
    flash, render_template,
    request, redirect, session, url_for)
from bson.objectid import ObjectId
from cocktails import app, db, mongo
from cocktails.models import Category, Users


@app.route("/")
@app.route("/get_cocktails")
def get_cocktails():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("cocktails.html", cocktails=cocktails)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        cocktail = {
            "category_id": request.form.get("category_id"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_description": request.form.get("cocktail_description"),
            "main_ingredient": request.form.get("main_ingredient"),
            # "created_by": session["user"],
            "method": request.form.get("method"),
            "other_ingredient": request.form.getlist("other_ingredient"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings")
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Cocktail Successfully Added")
        return redirect(url_for("get_cocktails"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add_cocktail.html", categories=categories)


@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    if request.method == "POST":
        submit = {
            "category_id": request.form.get("category_id"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_description": request.form.get("cocktail_description"),
            "main_ingredient": request.form.get("main_ingredient"),
            # "created_by": session["user"],
            "method": request.form.get("method"),
            "other_ingredient": request.form.getlist("other_ingredient"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings")
        }
        mongo.db.cocktails.update_one({"_id": ObjectId(cocktail_id)}, {"$set": submit})
        flash("Cocktail Successfully Updated")

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("edit_cocktail.html", cocktail=cocktail, categories=categories)
