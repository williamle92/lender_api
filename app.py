from flask import Flask
from flask_migrate import Migrate
from config import Config
from db import db
from flask_restful import Api,Resource


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app,db)
db.init_app(app)
api=Api(app)


@app.route("/")
def home():
    return "Hello World!"







if __name__ == "__main__":
    app.run()