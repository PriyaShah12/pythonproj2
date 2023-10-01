from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from pages import base_page
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class Test_search:

    def test_search_result(self, init_driver):
        print("I am in test_search_result")
        self.driver = init_driver
        print("Driver is -> ", self.driver)
        # self.bp = BasePage(self.driver)
        self.driver.get("https://google.com/")
        self.driver.maximize_window()
        time.sleep(2)
        text_field = self.driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
        text_field.send_keys("Sharukh khan")
        time.sleep(3)
        all_links = self.driver.find_elements(By.XPATH,"//ul[@class='G43f7e' and @ role = 'listbox'][1]/li")
        for x in all_links:
            print(x.text)

    def test_search_shoes(self, init_driver):
        print("I am in test_search_result")
        self.driver = init_driver
        print("Driver is -> ", self.driver)
        # self.bp = BasePage(self.driver)
        self.driver.get("https://google.com/")
        self.driver.maximize_window()
        time.sleep(2)
        text_field = self.driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
        text_field.send_keys("Shoes")
        time.sleep(3)
        all_links = self.driver.find_elements(By.XPATH, "//ul[@class='G43f7e' and @ role = 'listbox'][1]/li")
        for x in all_links:
            print(x.text)

