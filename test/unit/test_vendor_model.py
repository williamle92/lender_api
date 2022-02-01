import pytest
from models.vendor import VendorModel
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

    
