import allure

from pages.base_page import BasePage
from locators import HomePageLocators


class HomePage(BasePage):

    @allure.step('Нажимаем кнопку создания заказа в хэдере')
    def click_header_button(self):
        self.click(HomePageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Нажимаем большую кнопку создания заказа на странице')
    def click_big_button(self):
        self.click(HomePageLocators.ORDER_BUTTON_BIG)
