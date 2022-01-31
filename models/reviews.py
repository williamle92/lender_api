from db import db


class ReviewModel(db.Model):
    '''
    Review Object
    Represents the review object in the table review
    '''

    __tablename__ = "review"
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(1000), nullable= False)
    rating =db.Column(db.Integer, nullable=False)
    review_type = db.Column(db.String(50))
    loan_type = db.Column(db.String(50))
    author_name = db.Column(db.String(50), db.ForeignKey('author.name'), nullable=False)
    vendor_name = db.Column(db.String(50), db.ForeignKey('vendor.name'), nullable=False)


    def __init__(self, title, content, rating, review_type, loan_type, author_name, vendor_name):
        self.title = title
        self.content = content
        self.rating = rating
        self.review_type = review_type
        self.loan_type = loan_type
        self.author_name = author_name
        self.vendor_name = vendor_name


    def json(self):
        return {"title": self.title, "loan type": self.loan_type, "review type": self.review_type, "rating": self.rating, "author name": self.author_name, "vendor name": self.vendor_name, "content": self.content}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(self, id):
        return ReviewModel.query.filter_by(id=id).first()


    def __repr__(self):
        return f"Review \ntitle: {self.title}"