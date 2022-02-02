import pytest
from models.author import AuthorModel
from models.reviews import ReviewModel
from models.lender import LenderModel


def test_review():
    a = AuthorModel("johnsmith", "Irvine")
    v = LenderModel("Test Lender", "test summary")
    review = ReviewModel("title", "test", 5, "review type", "loan type", "johnsmith", "Test Lender", "January 2022")

    assert review.title == "title" and review.rating == 5
    assert review.author_name == "johnsmith" and review.lender_name == "Test Lender" and review.date_posted == "January 2022"