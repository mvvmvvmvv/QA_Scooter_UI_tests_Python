from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import FaqAccordionLocators


class FaqAccordionBlock:
    accordion_index_list = ["0", "1", "2", "3", "4", "5", "6", "7"]

    def __init__(self, driver):
        self.driver = driver

    def click_accordion_item(self, index):
        accordion_heading_locator = \
            FaqAccordionLocators.ACCORDION_BUTTON_LOCATOR.format(self.accordion_index_list[index])

        important_questions = self.driver.find_element(*FaqAccordionLocators.FAQ_HEADING)
        self.driver.execute_script("arguments[0].scrollIntoView();", important_questions)

        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, accordion_heading_locator))).click()

    def get_accordion_text(self, index):
        accordion_answer_locator = \
            FaqAccordionLocators.ACCORDION_PANEL_LOCATOR.format(self.accordion_index_list[index])
        return self.driver.find_element((By.XPATH, accordion_answer_locator)).get_attribute('innerHTML')




