from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse=True)#if we dont provide any scope then by default it is for all functions/methods whereever method name is passed as paramter
def init_driver(browser = "Chrome"):
    # global driver
    if browser == 'Chrome':
        s = Service(executable_path= "C:\\Priya_Dev\\chromedriver\\chromedriver.exe")
        print(s)
        driver = webdriver.Chrome(service=s)
    else:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()  #init_driver method will hold driver as its value and can be used by anymethod parameter in any file.



