from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON_IN_HEADER = [By.CLASS_NAME, 'Button_Button__ra12g']
    ORDER_BUTTON_BIG = [By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp']


class FaqAccordionLocators:
    FAQ_HEADING = [By.XPATH, ".//div[text()='Вопросы о важном'"]
    ACCORDION_BUTTON_LOCATOR = 'accordion__heading-{}'
    ACCORDION_PANEL_LOCATOR = 'accordion__panel-{}'


class RentFormDetailsLocators:
    DATE_FIELD = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    ENABLE_DATE_PICKER = [By.XPATH, ".//div[@tabindex='0']"]

    RENT_LENGTH_FIELD = [By.XPATH, ".//div[@class='Dropdown-control']"]

    CHECKBOX_BLACK = [By.ID, "black"]
    CHECKBOX_GREY = [By.ID, "grey"]

    COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    SUBMIT_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    BACK_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']


