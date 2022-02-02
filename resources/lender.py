from flask_restful import Resource, reqparse
from models.lender import LenderModel



class LenderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type=str, required=True, help="Must contain key (name) and value as a string in JSON request")
       
    def get(self, id):
        lender = LenderModel.find_by_id(id)
        if not lender:
            return {"Message": "The lender ID does not exist, please try again using a different ID"}, 404
        return lender.json()

    def post(self):
        data = LenderResource.parser.parse_args()

        #  lender is instantiated using key word arguments from the request
        lender = LenderModel(**data)

        try:
            lender.save_to_db()
        except:
            return {"Message": "An error occured while trying to create a lender"}, 500
        return lender.json(), 201

    def delete(self, id):
        lender = LenderModel.find_by_id(id)
        if lender:
            lender.delete_from_db()
        return {"Message": "Item deleted"}

    
    def put(self, id):
        data = LenderResource.parser.parse_args()
        lender = LenderModel.find_by_id(id)

        if lender is None:
            lender = LenderModel(**data)
        else:
            lender.name = data['name']
        lender.save_to_db()
        return lender.json()


class LenderList(Resource):
    def get(self):
        return {"type": "Lenders", "data": [v.json() for v in LenderModel.query.all()]}