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
