import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from urls import Urls


@pytest.fixture
def driver():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.maximize_window()
    browser.get(Urls.HOME_PAGE)
    yield browser
    browser.quit()
