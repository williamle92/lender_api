from flask import Flask
from flask_migrate import Migrate
from config import Config
from db import db
from flask_restful import Api
from resources.reviews import ReviewResource, Reviews
from resources.vendor import Vendor, VendorList


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app,db)
db.init_app(app)
api=Api(app)


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