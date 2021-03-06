from xml.dom.pulldom import ErrorHandler
from flask import Flask
from flask_migrate import Migrate
from config import Config
from db import db
from flask_restful import Api
from resources.author import AuthorList, AuthorResource
from resources.reviews import ReviewResource, Reviews
from resources.lender import LenderResource, LenderList

# Instantiate Flask app
app = Flask(__name__)

# Setting configs from Config object
app.config.from_object(Config)

# Instantiate migrate object
migrate = Migrate(app,db)

# Instantiate db
db.init_app(app)

# Custom Error handling
errors = {
    'Conflict': {
        'message': "The request could not be completed due to a conflict with the current state of the resource.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
    },
    "NotFound": {
        "status": 404,
        "message": "Not Found: The requested URL was NOT FOUND on the server. Please try again."
    },
    "InternalServerError":{
        "message": "Internal Server Error: The server encountered an unexpected condition which prevented it from fulfilling the request.",
        "status": 500
    }, 
    "BadRequest": {
        "message": "Bad Request: The request cannot be fulfilled due to bad syntax.",
        "status": 400,
    }, 
    "Unauthorized":{
        "message": "Unauthorized: Access is denied due to invalid credentials",
        "status": 401
    }
}

# Instantiate api object
api=Api(app, catch_all_404s=True, errors=errors)

# temporary view
@app.route("/")
def home():
    return "Hello World!"





# Adding the routes to our API
api.add_resource(LenderResource, "/reviews/lender/<id>", "/reviews/lender")
api.add_resource(LenderList, "/reviews/lenders")
api.add_resource(ReviewResource, "/review/<id>", "/review")
api.add_resource(Reviews, "/reviews")
api.add_resource(AuthorResource, "/reviews/author/<name>", "/reviews/author")
api.add_resource(AuthorList, "/reviews/authors")


if __name__ == "__main__":
    app.run()