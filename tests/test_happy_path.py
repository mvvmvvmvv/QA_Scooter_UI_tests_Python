import allure
import pytest
from pages.home_page import HomePage
from pages.rent_form_personal_page import RentFormPersonalPage
from pages.rent_form_details_page import RentFormDetailsPage
from pages.order_confirmation_page import OrderConfirmationPage


class TestHappyPath:
    @pytest.mark.parametrize(
        'first_name, second_name, address, metro, mobile, duration_option, color, comment, date',
        [
            ["Николай", "Расторгуев", "Петровка, 38", "Таганская", "89112128506", 3, "Black", "Атас!", "31.12.2022"],
            ["Перегрин", "Тук", "Туда и обратно", "Лубянка", "89119117766", 2, "Grey", "Абырвалг!", "10.12.2022"]
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
        personal_info.input_first_name(first_name)
        personal_info.input_second_name(second_name)
        personal_info.input_address(address)
        personal_info.input_metro(metro)
        personal_info.input_telephone(mobile)
        personal_info.click_continue()

        details = RentFormDetailsPage(driver)
        details.select_length(duration_option)
        details.select_color(color)
        details.write_comment(comment)
        details.input_date(date)
        details.submit_order()

        confirmation_page = OrderConfirmationPage(driver)
        confirmation_page.click_yes()
        confirmation_page.validate_order_confirmation()








