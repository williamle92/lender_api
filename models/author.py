from db import db

class AuthorModel(db.Model):
    '''
    Author Model
    Represent objects who compose the review and contained in table: author
    '''

    __tablename__ = "author"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50))
    reviews = db.relationship("ReviewModel", backref="author", lazy="dynamic")



    def __init__(self, name, city):
        self.name = name
        self.city = city


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"type": "author",
            "id": self.id,
            "name": self.name,
            "city": self.city,
        }

    @classmethod
    def find_by_username(self, name):
        return AuthorModel.query.filter_by(name=name).first()
        
    def __repr__(self):
        return f"Author: {self.name}, {self.city}"