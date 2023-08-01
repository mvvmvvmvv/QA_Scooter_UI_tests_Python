import allure
import pytest
from pages.home_page import HomePage
from pages.rent_form_personal_page import RentFormPersonalPage
from pages.rent_form_details_page import RentFormDetailsPage
from pages.order_confirmation_page import OrderConfirmationPage
from data import HappyPathTestData as Data


class TestHappyPath:
    @pytest.mark.parametrize(
        'first_name, second_name, address, metro, mobile, duration_option, color, comment, date',
        [
            Data.iteration_one,
            Data.iteration_two
        ]
    )
    @allure.title('Проверяем позитивный сценарий оформления заказа')
    def test_faq_accordion_shows_relevant_answer(self, driver,
                                                 first_name,
                                                 second_name,
                                                 address,
                                                 metro,
                                                 mobile,
                                                 duration_option,
                                                 color,
                                                 comment,
                                                 date):
        home_page = HomePage(driver)
        home_page.click_header_button()

        personal_info = RentFormPersonalPage(driver)
        personal_info.fill_personal_data_page(first_name, second_name, address, metro, mobile)

        details = RentFormDetailsPage(driver)
        details.fill_details_page(date, duration_option, color, comment)

        confirmation_page = OrderConfirmationPage(driver)
        confirmation_page.click_yes()
        confirmation_page.validate_order_confirmation()








