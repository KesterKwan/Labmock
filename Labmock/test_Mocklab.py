import Mocklab as mock

def test_is_palindrome_true():
    assert mock.is_palindrome("madam")==True

def test_is_palindrome_false():
    assert mock.is_palindrome("apple")==False

def test_is_palindrome_case_insensitive():
    assert mock.is_palindrome("RaceCar") == True
