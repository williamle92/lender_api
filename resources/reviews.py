from flask_restful import Resource, reqparse
from models.reviews import ReviewModel
from models.vendor import VendorModel
from models.author import AuthorModel


class ReviewResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Must contain key (title) and value as a string in JSON request")
    parser.add_argument('content', type=str, required=True, help="Must contain key (content) and value as a string in JSON request")
    parser.add_argument('rating', type=int, required=True, help="Must contain key (rating) and value as an integer in JSON request")
    parser.add_argument("review_type", type=str, required=True, help="Must contain key/value (review_type) and value as a string in JSON request")
    parser.add_argument("loan_type", type=str, required=True, help="Must contain key (loan_type) and value as a string in JSON request")
    parser.add_argument("author_name", type=str, required=True, help="Must contain key (author_name) and value as a string in JSON request")
    parser.add_argument('vendor_name', type=str, required=True, help="Must contain key(vendor_name) and value as a string in JSON request")

    def get(self, id):
        review = ReviewModel.find_by_id(id)
        if not review:
            return {"Message": "The review does not exist, please try again."}, 404
        return review.json(), 200

    def post(self):
        data = ReviewResource.parser.parse_args()
        author_exist = AuthorModel.find_by_username(data["author_name"])
        vendor_exist = VendorModel.find_by_id(id=None, name=data['vendor_name'])

        if not author_exist:
            return {"Message": "The author in the request does not exist, please try again"}
        if not vendor_exist:
            return {"Message": "The vendor in the request does not exist, please try again"}