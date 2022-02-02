import pytest
from models.lender import VendorModel
from models.reviews import ReviewModel



def test_vendor_name():
    test_vendor = VendorModel("Test Lender")
    assert test_vendor.name == "Test Lender"


def test_empty_string():
    v = VendorModel("")
    assert v.name == ""


def test_no_instantiation():
    with pytest.raises(TypeError):
        test = VendorModel()
        test


def test_vendor_review():
    review = ReviewModel("title", "test", 5, "review type", "loan type", "johnsmith", "Test Lender")
    test_vendor = VendorModel("Test Lender")
    test_vendor.reviews.append(review)

    assert test_vendor.reviews 
    

