from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en")


@pytest.fixture(scope="function")
def browser(request, browser=None):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(firefox_profile=fp)

    yield browser
    print("\nQuit browser...")
    browser.quit
