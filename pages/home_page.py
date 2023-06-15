from base_page import BasePage
from locators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_header_button(self):
        BasePage.click(self.driver, HomePageLocators.ORDER_BUTTON_IN_HEADER)

    def click_big_button(self):
        BasePage.click(self.driver, HomePageLocators.ORDER_BUTTON_BIG)
