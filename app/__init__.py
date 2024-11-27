# To install flask, first run the following line in the terminal:
# pip install flask
# pip install python-dotenv

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sentry_sdk

load_dotenv()

sentry_dsn = os.environ["SENTRY_DSN"]

sentry_sdk.init(
    dsn=sentry_dsn,
)
flask_app = Flask(__name__)

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ.get("MONGODB_PASSWORD")

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.app  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

from app import routes