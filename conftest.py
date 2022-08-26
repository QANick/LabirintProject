import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.app import Application
from constants import LoginMessages


@pytest.fixture
def app():
    url = 'https://www.labirint.ru/'
    chrome_options = Options()
    chrome_options.add_argument("window-size=1800,1080")
    driver = webdriver.Chrome('/Users/nick/chromedriver')
    app = Application(driver, url)
    yield app
    app.quit()

@pytest.fixture
def my_cabinet(app):
    app.login_page.open_login_page()
    username = LoginMessages.LOGIN
    password = LoginMessages.PASSWORD
    app.login_page.entry_data(username=username, password=password)
    assert app.login_page.get_relative_link() == '/cabinet/'



