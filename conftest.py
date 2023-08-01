import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(Urls.HOME_PAGE)
    yield browser
    browser.quit()
