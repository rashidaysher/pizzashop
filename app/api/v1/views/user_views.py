from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.api.v1.models.user_models import Customer, Pizza

parser = RequestParser

parser.add_argument("phonenumber", type=str, required=True, help="Please input a phonenumber")
parser.add_argument("username", type=str, required=True, help="Please input your name")

class Customer (Resource):
    """
    Customer endpoint
    """

    def post(self):
        """
        Enter a customer
        """
        args = parser.parse_args()
        username = args["username"]
        phonenumber = args["phonenumber"]
        password = args["password"]

        newCustomer = Customer(username, phonenumber, password)
        newCustomer.save_customer()

        return {
            "message": "Welcome to PizzaApp",
            "user" : newCustomer.__dict__
        }, 201

class Pizza(Resource):

    def get(self):
        """
        Get a list of Pizza
        """
        args = parser.parse_args()
        name = args["name"]
        id = args["id"]

        newPizza = Pizza(name,id)
        newPizza.save_pizza()

        return {
            "message": "This are the Pizzas available",
            "user" : newPizza.__dict__
        }, 201

