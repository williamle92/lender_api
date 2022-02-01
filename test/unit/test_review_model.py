import pytest
from models.author import AuthorModel
from models.reviews import ReviewModel
from models.vendor import VendorModel


def test_review():
    a = AuthorModel("johnsmith", "Irvine")
    v = VendorModel("Test Lender")
    review = ReviewModel("title", "test", 5, "review type", "loan type", "johnsmith", "Test Lender")

    assert review.title == "title" and review.rating == 5
    assert review.author_name == "johnsmith" and review.vendor_name == "Test Lender"