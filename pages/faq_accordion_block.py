import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import FaqAccordionLocators
from pages.base_page import BasePage


class FaqAccordionBlock(BasePage):

    @allure.step('Открываем блок ЧаВО')
    def click_accordion_item(self, index):
        accordion_heading_locator = \
            FaqAccordionLocators.ACCORDION_BUTTON_LOCATOR.format(index)

        important_questions = self.find_element_located(FaqAccordionLocators.FAQ_SCROLL_ANCHOR)
        self.scroll_to_element_script(important_questions)

        accordion_item = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located((By.ID, accordion_heading_locator)))
        accordion_item.click()

    @allure.step('Получаем текст ответа')
    def get_accordion_text(self, index):
        accordion_answer_locator = \
            FaqAccordionLocators.ACCORDION_PANEL_LOCATOR.format(index)
        return self.find_element_located((By.ID, accordion_answer_locator)).text




