
import pytest
from models.author import AuthorModel
from models.reviews import ReviewModel
from models.lender import VendorModel

# run using command python -m (for module) pytest
def test_NewAuthor():
    '''
    GIVEN a Author model
    WHEN a new author is created
    THEN check if name or city are defined correctly
    '''
    
    test_author = AuthorModel("JohnSmith90", "Irvine")
    assert test_author.name == "JohnSmith90" and test_author.city == "Irvine"
    


def test_author_no_name():
    with pytest.raises(TypeError):
        test_author_no_name = AuthorModel( "Irvine")
        test_author_no_name


def test_author_lower_name():
    test_author_same_name_lower = AuthorModel("johnsmith90", "Irvine")
    assert test_author_same_name_lower.name == "johnsmith90"

def test_author_city_empty_string():
    test_author_no_city = AuthorModel("lender2020", "")
    assert test_author_no_city.city == ""

def test_empty_strings():
    test_author_blank = AuthorModel("", "")
    assert test_author_blank.name == "" and test_author_blank.city==""


def test_int_name():
    test_author_int = AuthorModel(112121, "irvine")
    assert test_author_int.name == 112121