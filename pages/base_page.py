import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def write_text(self, element, text):
        self.driver.find_element(*element).send_keys(text)


