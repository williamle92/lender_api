import pytest
from models.lender import LenderModel
from models.reviews import ReviewModel



def test_lender_name():
    test_lender = LenderModel("Test Lender", "test summary")
    assert test_lender.name == "Test Lender" and test_lender.summary == "test summary"


def test_empty_string():
    v = LenderModel("", "")
    assert v.name == "" and v.summary == ""


def test_no_instantiation():
    with pytest.raises(TypeError):
        test = LenderModel()
        test


def test_lender_review():
    review = ReviewModel("title", "test", 5, "review type", "loan type", "johnsmith", "Test Lender", "January 2022")
    test_lender = LenderModel("Test Lender", "test summary")
    test_lender.reviews.append(review)

    assert test_lender.reviews 
    

