from flask_restful import Resource, reqparse
from models.reviews import ReviewModel
from models.lender import LenderModel
from models.author import AuthorModel


class ReviewResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Must contain key (title) and value as a string in JSON request")
    parser.add_argument('content', type=str, required=True, help="Must contain key (content) and value as a string in JSON request")
    parser.add_argument('rating', type=int, required=True, help="Must contain key (rating) and value as an integer in JSON request")
    parser.add_argument("review_type", type=str, required=True, help="Must contain key/value (review_type) and value as a string in JSON request")
    parser.add_argument("loan_type", type=str, required=True, help="Must contain key (loan_type) and value as a string in JSON request")
    parser.add_argument("author_name", type=str, required=True, help="Must contain key (author_name) and value as a string in JSON request")
    parser.add_argument('lender_name', type=str, required=True, help="Must contain key(lender_name) and value as a string in JSON request")
    parser.add_argument("date_posted", type=str, required=True, help="Must contain key(date_posted) and value as a string in JSON request")

    def get(self, id):
        review = ReviewModel.find_by_id(id)
        if not review:
            return {"Message": "The review does not exist, please try again."}, 404
        return review.json(), 200

    def post(self):
        data = ReviewResource.parser.parse_args()
        author_exist = AuthorModel.find_by_username(data["author_name"])
        lender_exist = LenderModel.find_by_id(id=None, name=data['lender_name'])

        if not author_exist:
            return {"Message": "The author in the request does not exist, please try again"}
        if not lender_exist:
            return {"Message": "The lender in the request does not exist, please try again"}
        review = ReviewModel(**data)
        try:
            review.save_to_db()
        except:
            return {"Message": "An error occurred while processing the request, please try again"}
        return review.json()


    def delete(self, id):
        review = ReviewModel.find_by_id(id)
        if not review:
            return {"Message": "The review could not be found, please try again!"}
        review.delete_from_db()
        return {"Message": "Review has been deleted from the database"}

    
    def put(self, id):
        data = ReviewResource.parser.parse_args()
        review = ReviewModel.find_by_id(id)

        if not review:
            review = ReviewModel(**data)
        else:
            review.title = data["title"]
            review.content = data['content']
            review.rating = data["rating"]
            review.review_type= data["review_type"]
            review.loan_type = data["loan_type"]
            review.author_name = data["author_name"]
            review.lender_name = data["lender_name"]

        review.save_to_db()
        return review.json()


class Reviews(Resource):
    def get(self):
        return {"type": "reviews", "data":[review.json() for review in ReviewModel.query.all()]}