import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("launch chrome")
    elif browser == "ff":
        print("launch ff")
    else:
        print("provide valid browser")
    print("Launch browser")
    print("Login")
    print("browse products")
    yield
    print("Logoff")
    print("close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")