from db import db
from sqlalchemy.ext.hybrid import hybrid_property

class VendorModel(db.Model):
    '''
    Vendor Model
    Represents an internal object located in table vendor
    '''

    __tablename__ = "vendor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    reviews = db.relationship('ReviewModel', backref="vendormodel", lazy="dynamic")


    def __init__(self, name):
        self.name = name
    
    # Creates a property number of reviews. {.num_review} property name
    @hybrid_property
    def num_review(self):
        return len(self.reviews)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"type": "vendor", "id": self.id, "name": self.name}

    # Decorator allows methods to be executed on class without creating an instance
    @classmethod
    def find_by_id(self, id, name=None):
        if name:
            return VendorModel.query.filter_by(name=name).first()
        return VendorModel.query.filter_by(id=id).first()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()