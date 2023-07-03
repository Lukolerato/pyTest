#writing methods to test
import pytest

@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


@pytest.mark.sanity
def testLogin(demo_fixture):
    print("Login Successful")


# def testLogoff():
#     print("Logoff Successful")
#
# def testCalculation():
#     assert 2 + 2 == 4
