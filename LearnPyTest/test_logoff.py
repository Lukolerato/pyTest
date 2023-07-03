#writing methods to test

#first browse products then add items
import pytest

'''@pytest.fixture
def setUp():
    print("Launch browser")
    print("Login")
    print("browse products")
    yield #here is goting to be additem executed
    print("Logoff")
    print("close browser")'''

def testAddItemToCart(tc_setup):
    print("add item")

def testRemoveItemFromCart(tc_setup):
    print("remove items")
