
from db import db
from sqlalchemy.ext.hybrid import hybrid_property

class LenderModel(db.Model):
    '''
    Lender Model
    Represents an internal object located in table lender
    '''

    __tablename__ = "lender"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    summary = db.Column(db.String(1000))
    reviews = db.relationship('ReviewModel', backref="lender", lazy="dynamic")


    def __init__(self, name, summary):
        self.name = name
        self.summary = summary

    # Creates a property number of reviews. {.num_review} property name
    @hybrid_property
    def num_review(self):
        return len(self.reviews)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"type": "lender", "id": self.id, "name": self.name, "summary": self.summary}

    # Decorator allows methods to be executed on class without creating an instance
    @classmethod
    def find_by_id(self, id, name=None):
        if name:
            return LenderModel.query.filter_by(name=name).first()
        return LenderModel.query.filter_by(id=id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Lender: {self.name}"