# from pages.order_page import OrderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)

    def quit(self):
        self.driver.quit()

