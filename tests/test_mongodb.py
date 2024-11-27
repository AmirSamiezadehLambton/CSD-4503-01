from pymongo import MongoClient
from dotenv import load_dotenv
import os
import unittest
from app import flask_app


class MongoDBTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        # Set up the test client
        db_username = os.environ["MONGODB_USERNAME"]
        db_password = os.environ.get("MONGODB_PASSWORD")
        self.client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    def test_connection(self):
        # print(self.client.list_database_names())
        response = self.client.admin.command('ping')
        print(response)




