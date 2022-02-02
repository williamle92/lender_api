from xml.dom.pulldom import ErrorHandler
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from config import Config
from db import db
from flask_restful import Api
from resources.reviews import ReviewResource, Reviews
from resources.vendor import Vendor, VendorList

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
        "message": "Not Found: The requested URL was NOT FOUND on the server. Please try again.",
        "extra": "Make sure the request follows the following format:http://127.0.0.1:5000/vendor/<id> "
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
api.add_resource(Vendor, "/vendor/<id>", "/vendor")
api.add_resource(VendorList, "/vendors")
api.add_resource(ReviewResource, "/review/<id>", "/review")
api.add_resource(Reviews, "/reviews")



if __name__ == "__main__":
    app.run()