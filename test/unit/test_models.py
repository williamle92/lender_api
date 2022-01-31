
from models.author import AuthorModel
from models.reviews import ReviewModel
from models.vendor import VendorModel


def test_NewAuthor():
    '''
    GIVEN a Author model
    WHEN a new author is created
    THEN check if name are defined correctly
    '''
    
    test_author = AuthorModel("JohnSmith90", "Irvine")
    test_author_same_name = AuthorModel("johnsmith90", "Irvine")
    test_author_no_city = AuthorModel("lender2020", "")
    test_author_no_name = AuthorModel("", "Irvine")
    test_author_int = AuthorModel(112121, "irvine")
    test_author_blank = AuthorModel("", "")


    assert test_author.name == "JohnSmith90" and test_author.city == "Irvine"
    