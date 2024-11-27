from app import flask_app, products_collection
from flask import render_template

@flask_app.route("/index", methods=["GET"])
def index():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    return "This is the index page!"


@flask_app.route("/")
def home():
    return render_template("index.html")
    # return "This is the index page!"


@flask_app.route("/products")
def products():
    # Fetch all products from MongoDB
    products = list(products_collection.find())
    return render_template("products.html", products=products)
