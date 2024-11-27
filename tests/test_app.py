# the file name for unit testing must follow this convention: test_<something>
from app import flask_app
import unittest

# class to represent the test cases
# use functions (methods) to define the scenarios

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_index_1(self):
        # Send a GET request to the "/" route
        response = self.app.get("/")

        # Check if the response is 200 OK
        self.assertEqual(first=response.status_code, second=200)

    def test_index_2(self):
        # Send a GET request to the "/" route
        response = self.app.post("/")

        # Check if the response is 200 OK
        self.assertEqual(first=response.status_code, second=405)


    # def test_index_2(self):
    #     # Send a GET request to the "/" route
    #     response = self.app.get("/index")
    #
    #     # Check if the response is 200 OK
    #     self.assertEqual(first=response.status_code, second=200)
    #
    # def test_index_data(self):
    #     # Send a GET request to the "/" route
    #     response = self.app.get("/index")
    #
    #     # Check if the response is 200 OK
    #     self.assertEqual(first=response.data.decode('utf-8'), second="This is the index page!")

