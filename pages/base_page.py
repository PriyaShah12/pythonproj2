from test_cases.conftest import init_driver
import pytest

class BasePage():
    """This is base page constructor which will be parent of all pages constructor"""
    def __init__(self, driver):
        self.driver = driver
        print("constructor called*****")



