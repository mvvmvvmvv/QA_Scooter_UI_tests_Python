from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def write_text(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    def find_element_located(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
