from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def user_language_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit
