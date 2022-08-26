from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import urlparse
import time


class LoginPage(BasePage):
    BUTTON_CABINET = (By.XPATH, "//*[@href='/cabinet/']")
    BUTTON_MY_LABIRINT = (By.XPATH, "//*[@class ='b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   b-header-e-sprite-background']")
    INPUT_FIELD_FOR_EMAIL = (By.NAME, "code")
    BUTTON_ENTER = (By.ID, "g-recap-0-btn")
    INPUT_FIELD_FOR_SALE_CODE = (By.CLASS_NAME, "full-input__input.formvalidate-error")
    BUTTON_CHECK_CODE_AND_ENTER = (By.XPATH, "//*[@id='auth-email-sent']/input[@type = 'submit']")
    ERROR_TEXT = (By.XPATH, "//small[contains(text(), 'Введенного кода не существует')]")
    BUTTON_COUPONS = (By.XPATH, "//*[@href='/cabinet/coupons/']")
    TEXT_CODE = (By.XPATH, "//small[contains(text(), 'Введенного кода не существует')]")
    BUTTON_MY_CABINET = (By.XPATH, "//*[@class ='b-header-b-personal-e-link top-link-main top-link-main_cabinet  js-b-autofade-wrap']")
    COUPON_BLOCK = (By.CSS_SELECTOR, "div.coupon-block")
    TITLE_NO_ORDERS = (By.XPATH, "//*[contains(text(), 'Вы пока не оформили ни одного заказа')]")
    BUTTON_WISH_LIST = (By.XPATH, "//*[@href='/cabinet/putorder/']")
    WISH_LIST_BLOCK = (By.CSS_SELECTOR, "div.product.need-watch.product_labeled.product-cart.watched")
    BUTTON_VIEWING_HISTORY = (By.XPATH, "//*[@href='/cabinet/?vybor=visited']")
    VIEWING_HISTORY_BLOCK = (By.CSS_SELECTOR, "span.navisort-head-text")
    BUTTON_COMPARE_LIST = (By.XPATH, "//*[@href='/compare/']")
    COMPARE_BUTTON_NUM = (By.CSS_SELECTOR, "span.compare-button__num")
    COMPARE_LIST_BLOCK = (By.CSS_SELECTOR, "div[data-incompare = '1']")
    BUTTON_CREATE_FOLDER = (By.XPATH, "//a[@class='btn btn-small btn-clear-blue mb15']")
    INPUT_FIELD_FOR_FOLDER_NAME = (By.ID, 'jsNameCat')
    BUTTON_CREATE = (By.XPATH, "//input[@value='Создать']")
    STRING_FOLDER = (By.XPATH, "//*[@class = 'grid-table border-folder-bottom link pb5 mb5 mh40']/div[@class = ' checkble grid-item_b break-word']")
    BUTTON_PERSONAL_DATA = (By.XPATH, "//*[@href='/cabinet/personal/']")
    BUTTON_SETTINGS = (By.XPATH, "//*[@href='/cabinet/settings/']")
    BUTTON_SUBSCRIPTIONS = (By.XPATH, "//*[contains(text(), 'Подписки')]")
    SUBSCRIPTIONS = (By.XPATH, "//ul[@class = 'availsubscr']")
    BUTTON_RECOMMENDATIONS = (By.XPATH, "//*[contains(text(), 'Рекомендации')]")
    RECOMMENDATIONS_BLOCK = (By.CSS_SELECTOR, "div.recommended__book-card-table")

    def open_login_page(self):
        """
        Open login page.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.BUTTON_MY_LABIRINT)

    def open_cabinet(self):
        """
        Open my cabinet.
        """
        self.click_element(locator=self.BUTTON_MY_LABIRINT)

    def entry_data(self, username, password):
        """
        Data entry in fields.
        """
        self.clear(locator=self.INPUT_FIELD_FOR_EMAIL)
        self.fill(locator=self.INPUT_FIELD_FOR_EMAIL, value=username)
        self.click_element(locator=self.BUTTON_ENTER)
        self.clear(locator=self.INPUT_FIELD_FOR_SALE_CODE)
        self.fill(locator=self.INPUT_FIELD_FOR_SALE_CODE, value=password)
        self.click_element(locator=self.BUTTON_CHECK_CODE_AND_ENTER)
        time.sleep(10)
        self.click_element(locator=self.BUTTON_MY_LABIRINT)

    def entry_invalid_code(self, username):
        """
        Invalid code entry in fields.
        """
        self.clear(locator=self.INPUT_FIELD_FOR_EMAIL)
        self.fill(locator=self.INPUT_FIELD_FOR_EMAIL, value=username)
        self.click_element(locator=self.BUTTON_ENTER)

    def entry_valid_email_and_invalid_code(self, username, password):
        """
        Invalid data entry in fields.
        """
        self.clear(locator=self.INPUT_FIELD_FOR_EMAIL)
        self.fill(locator=self.INPUT_FIELD_FOR_EMAIL, value=username)
        self.click_element(locator=self.BUTTON_ENTER)
        self.clear(locator=self.INPUT_FIELD_FOR_SALE_CODE)
        self.fill(locator=self.INPUT_FIELD_FOR_SALE_CODE, value=password)
        self.click_element(locator=self.BUTTON_CHECK_CODE_AND_ENTER)

    def text_error_invalid_data(self) -> str:
        """
        Errors on login page.
        """
        element = self.text(locator=self.ERROR_TEXT)
        return element

    def open_tab_coupons(self):
        """
        Open tab (page) "coupons"
        """
        self.click_element(locator=self.BUTTON_COUPONS)

    def open_tab_personal_data(self):
        """
        Open tab (page) "personal data"
        """
        self.click_element(locator=self.BUTTON_PERSONAL_DATA)

    def open_tab_settings(self):
        """
        Open tab (page) "settings"
        """
        self.click_element(locator=self.BUTTON_PERSONAL_DATA)
        self.click_element(locator=self.BUTTON_SETTINGS)
        time.sleep(2)

    def open_tab_viewing_history(self):
        """
        Open tab (page) "viewing history"
        """
        self.click_element(locator=self.BUTTON_VIEWING_HISTORY)

    def find_amount_of_items_in_viewing_history(self):
        """
        Get amount of book at tab(page) "viewing history"
        """
        self.click_element(locator=self.BUTTON_VIEWING_HISTORY)
        element = self.text(locator=self.VIEWING_HISTORY_BLOCK)
        list = []
        for i in element.split():
            try:
                list.append(int(i))
            except ValueError:
                pass
        return list[0]

    def find_amount_of_coupons(self):
        """
        Get amount of coupons at tab(page) "coupons"
        """
        self.click_element(locator=self.BUTTON_COUPONS)
        amount = self.list_of_all_elements(locator=self.COUPON_BLOCK)
        return len(amount)

    def find_amount_of_wish_list_items(self):
        """
        Get amount of book at tab(page) "wish list"
        """
        self.click_element(locator=self.BUTTON_WISH_LIST)
        amount = self.list_of_all_elements(locator=self.WISH_LIST_BLOCK)
        return len(amount)

    def find_amount_of_items_in_compare_list(self):
        """
        Get amount of book at tab(page) "compare list"
        """
        self.click_element(locator=self.BUTTON_COMPARE_LIST)
        amount = self.list_of_all_elements(locator=self.COMPARE_LIST_BLOCK)
        return len(amount)

    def find_amount_of_subscriptions(self):
        """
        Get amount of subscriptions
        """
        self.click_element(locator=self.BUTTON_PERSONAL_DATA)
        self.click_element(locator=self.BUTTON_SUBSCRIPTIONS)
        amount = self.list_of_all_elements(locator=self.SUBSCRIPTIONS)
        return len(amount)

    def find_amount_of_recommendations(self):
        """
        Get amount of subscriptions
        """
        self.click_element(locator=self.BUTTON_RECOMMENDATIONS)
        amount = self.list_of_all_elements(locator=self.RECOMMENDATIONS_BLOCK)
        return len(amount)

    def text_no_orders(self):
        """
        Get "No orders" text
        """
        element = self.text(locator=self.TITLE_NO_ORDERS)
        return element

    def get_relative_link(self):
        """
        Get relative link
        """
        url = urlparse(self.app.driver.current_url)
        return url.path
