from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.firefox.service import Service



@pytest.fixture()
def setup():
    s = Service("C:/Users/usman.ali/PycharmProjects/pythonProject/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    return driver


## Get chrome and FF to work
# @pytest.fixture()
# def setup(browser):
#     s = Service("C:/Users/usman.ali/PycharmProjects/pythonProject/chromedriver.exe")
#     f = Service("C:/Users/usman.ali/PycharmProjects/pythonProject/geckodriver.exe")
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=s)
#         driver.maximize_window()
#         print("Launching Chrome Browser")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(service=f)
#         driver.maximize_window()
#         print("Launching Firefox Browser")
#     else:
#         driver = webdriver.Chrome(service=s)
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

################## Pytest HTML Report #############################

def pytest_configure(config):
    config._metadata = {
        "Tester": "Usman",
        "Project Name": "Hybrid Framework Practice"}


# It is a hook for deleting/modifying environment info in the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)

