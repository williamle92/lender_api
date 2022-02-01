from flask_restful import Resource, reqparse
from models.vendor import VendorModel



class Vendor(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument("name",type=str, required=True, help="Must contain a vendor name (str) in request ")
    



    def get(self, id):
        vendor = VendorModel.find_by_id(id)
        if not vendor:
            return {"Message": "The vendor ID does not exist, please try again using a different ID"}, 404
        return vendor.json()

    def post(self):
        data = Vendor.parser.parse_args()

        #  vendor is instantiated using key word arguments from the request
        vendor = VendorModel(**data)

        try:
            vendor.save_to_db()
        except:
            return {"Message": "An error occured while trying to create a vendor"}, 500
        return vendor.json(), 201

    def delete(self, id):
        vendor = VendorModel.find_by_id(id)
        if vendor:
            vendor.delete_from_db()
        return {"Message": "Item deleted"}

    
    def put(self, id):
        data = Vendor.parser.parse_args()
        vendor = VendorModel.find_by_id(id)

        if vendor is None:
            vendor = VendorModel(**data)
        else:
            vendor.name = data['name']
        vendor.save_to_db()
        return vendor.json()


class VendorList(Resource):
    def get(self):
        return {"type": "vendor", "data": [v.json() for v in VendorModel.query.all()]}