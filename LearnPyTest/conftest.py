import pytest


@pytest.fixture
def tc_setup():
    print("Launch browser")
    print("Login")
    print("browse products")
    yield
    print("Logoff")
    print("close browser")