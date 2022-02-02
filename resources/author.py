from flask import jsonify
from flask_restful import Resource, reqparse
from models.author import AuthorModel


class AuthorResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Must contain key (name) and value as a string in JSON request")
    parser.add_argument('city', type=str, required=True, help="Must contain key (city) and value as a string in JSON request")

    # Since names are unique, we can take accept it as a parameter in get request
    def get(self, name):
        author = AuthorModel.find_by_username(name=name)
        if not author:
            return {"Message": "The author name does not exist, please try again using a different name"},404
        return author.json()

    def post(self):
        data = AuthorResource.parser.parse_args()

        author = AuthorModel(**data)
        try:
            author.save_to_db()
        except:
            return {"Message": "An error occured while trying to process the request"}, 500
        return author.json()

    def delete(self, name):
        author = AuthorModel.find_by_username(name=name)
        if author:
            author.delete_from_db()
        return {"Message": "Item deleted"}

    def put(self, name):
        data = AuthorResource.parser.parse_args()
        author = AuthorModel.find_by_username(name)

        if author is None:
            author = AuthorModel(**data)
        else:
            author.name = data["name"]
            author.city = data["city"]
        author.save_to_db()
        return author.json()


class AuthorList(Resource):
    def get(self):
        return {"type": "authors", "data": [a.json() for a in AuthorModel.query.all()]}