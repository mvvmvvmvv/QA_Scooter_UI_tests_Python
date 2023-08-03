import allure
import pytest
from pages.faq_accordion_block import FaqAccordionBlock
from data import AccordionTestData as Data


class TestFaq:

    @pytest.mark.parametrize(
        'index, answer',
        [
            Data.faq_item_0,
            Data.faq_item_1,
            Data.faq_item_2,
            Data.faq_item_3,
            Data.faq_item_4,
            Data.faq_item_5,
            Data.faq_item_6,
            Data.faq_item_7
        ]
    )
    @allure.title('Проверяем тексты всех ответов')
    def test_faq_accordion_shows_relevant_answer(self, driver, index, answer):
        accordion = FaqAccordionBlock(driver)

        accordion.click_accordion_item(index)
        actual_text = accordion.get_accordion_text(index)

        assert actual_text == answer, "Ответ не совпадает"