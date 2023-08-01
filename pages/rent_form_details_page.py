import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import RentFormDetailsLocators
from pages.base_page import BasePage


class RentFormDetailsPage(BasePage):

    @allure.step('Выбираем дату')
    def input_date(self, delivery_date):
        self.write_text(RentFormDetailsLocators.DATE_FIELD, delivery_date)
        self.find_element_located(RentFormDetailsLocators.DATE_FIELD).send_keys(Keys.RETURN)

    @allure.step('Выбираем срок аренды')
    def select_length(self, index):
        self.click(RentFormDetailsLocators.RENT_LENGTH_FIELD)
        how_long_option = RentFormDetailsLocators.DROPDOWN_OPTIONS_TEMPLATE\
            .format(RentFormDetailsLocators.DROPDOWN_OPTIONS_VALUES[index])
        self.click((By.XPATH, how_long_option))

    @allure.step('Выбираем цвет')
    def select_color(self, color):
        if color == "Black":
            self.click(RentFormDetailsLocators.CHECKBOX_BLACK)
        self.click(RentFormDetailsLocators.CHECKBOX_GREY)

    @allure.step('Пишем комментарий')
    def write_comment(self, comment):
        self.write_text(RentFormDetailsLocators.COMMENT, comment)

    @allure.step('Отправляем заказ')
    def submit_order(self):
        self.click(RentFormDetailsLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Заполняем всю форму деталей заказа')
    def fill_details_page(self, date, index, color, comment):
        self.input_date(date)
        self.select_length(index)
        self.select_color(color)
        self.write_comment(comment)
        self.submit_order()


