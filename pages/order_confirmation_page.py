import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import OrderConfirmationLocators
from pages.base_page import BasePage


class OrderConfirmationPage(BasePage):

    @allure.step('Подтверждаем заказ')
    def click_yes(self):
        self.click(OrderConfirmationLocators.CONFIRM_BUTTON)

    @allure.step('Проверяем что окно подтверждения заказа открылось')
    def validate_order_confirmation(self):
        WebDriverWait(self.driver, 3)\
            .until(EC.visibility_of_element_located(OrderConfirmationLocators.CONFIRMATION_MESSAGE))
