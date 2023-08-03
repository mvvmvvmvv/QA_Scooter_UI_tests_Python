import allure

from locators import RentFormPersonalLocators
from pages.base_page import BasePage


class RentFormPersonalPage(BasePage):

    @allure.step('Вводим имя')
    def input_first_name(self, first_name):
        self.write_text(RentFormPersonalLocators.FIRST_NAME, first_name)

    @allure.step('Вводим фамилию')
    def input_second_name(self, second_name):
        self.write_text(RentFormPersonalLocators.SECOND_NAME, second_name)

    @allure.step('Указываем адрес')
    def input_address(self, address):
        self.write_text(RentFormPersonalLocators.ADDRESS, address)

    @allure.step('Выбираем метро')
    def input_metro(self, metro):
        self.click(RentFormPersonalLocators.METRO)
        self.write_text(RentFormPersonalLocators.METRO, metro)
        self.click(RentFormPersonalLocators.DIV_LIST_HACK)

    @allure.step('Указываем телефон')
    def input_telephone(self, telephone):
        self.write_text(RentFormPersonalLocators.TELEPHONE, telephone)

    @allure.step('Подтверждаем и переходим на следующий шаг')
    def click_continue(self):
        self.click(RentFormPersonalLocators.CONTINUE_BUTTON)

    @allure.step('Заполняем всю форму личных данных')
    def fill_personal_data_page(self, first_name, second_name, address, metro, telephone):
        self.input_first_name(first_name)
        self.input_second_name(second_name)
        self.input_address(address)
        self.input_metro(metro)
        self.input_telephone(telephone)
        self.click_continue()

