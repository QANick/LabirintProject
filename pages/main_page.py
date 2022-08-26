from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urllib.parse import urlparse
import time


class MainPage(BasePage):

    BUTTON_BOOKS = (By.XPATH, "//*[@href='/books/']")
    BUTTON_MY_LABIRINT = (By.XPATH, "//*[@class ='b-header-b-personal-e-icon b-header-b-personal-e-icon-m-profile   b-header-e-sprite-background']")
    BUTTON_BEST_AT_2022 = (By.XPATH, "//span[@class = 'b-header-b-menu-e-link']/a[@href='/best/']")
    BUTTON_CLUB = (By.XPATH, "//*[@href='/club/']")
    BUTTON_ACTIONS = (By.XPATH, "//*[@href='/actions/']")
    BUTTON_SUPPORT = (By.XPATH, "//*[@href='/support/']")
    BUTTON_NEW_BOOKS = (By.XPATH, "//*[@href='/novelty/']")
    BUTTON_CART = (By.XPATH, "//li/a[@href='/cart/']")
    BUTTON_TO_DO_ORDER = (By.XPATH, "//button[@type='submit']")
    BUTTON_WISH_LIST = (By.XPATH, "//li/a[@href='/cabinet/putorder/']")
    BUTTON_SEARCH = (By.XPATH, "//button[@class='b-header-b-search-e-btn']")
    BUTTON_VIDEO = (By.XPATH, "//*[contains(text(), 'Видео')]")
    BUTTON_CLEAR_WISH_LIST = (By.XPATH, "//a[@title='Удалить все отложенные товары']")
    BUTTON_ADD_IN_CART = (By.XPATH, "//div[@class='product-buy buy-avaliable fleft']")
    BUTTON_ADD_IN_CART_ON_BOOK_PAGE = (By.XPATH, "//span[contains(text(), 'Добавить')]")
    BUTTON_ADD_IN_WISH_LIST = (By.CSS_SELECTOR, 'a.icon-fave.track-tooltip.js-open-deferred-block ')
    BUTTON_ACCEPT = (By.XPATH, "//div[@class='base-button--content']")
    BUTTON_HELP = (By.XPATH, "//a[@href='/help/']")
    BUTTON_MAPS = (By.XPATH, "//a[@href='/maps/']")
    BUTTON_SCHOOL = (By.CSS_SELECTOR, "a[title = 'Школа']")
    BUTTON_ELSE = (By.XPATH, "//span[@class = 'b-header-e-sprite-background dots-icon']")
    BUTTON_GAMES = (By.XPATH, "//a[@href='/games']")
    ACCEPTED_COUPON = (By.XPATH, "//span[contains(text(), 'Применен 1 купон')]")
    QUANTITY = (By.XPATH, "//div/input[@class='quantity']")
    BUTTON_ADD_COUPONS = (By.XPATH, "//button[contains(text(), 'Добавить купоны')]")
    BOOKS_IN_CART_ICON = (By.XPATH, "//span[@class='b-header-b-personal-e-icon-count-m-cart basket-in-cart-a']")
    BOOKS_IN_WISH_LIST_ICON = (By.XPATH, "//span[@class='b-header-b-personal-e-icon-count-m-putorder basket-in-dreambox-a']")
    VIDEO_BLOCK = (By.XPATH, "//a[@class='rubric-list-item videobloc-carousel-item js-videoblock-video-show']")
    NAME_BOOK = (By.XPATH, "//a[@class='product-title-link']")
    CERTIFICATE_BLOCK = (By.XPATH, "//div[@class = 'product-padding product-padding-cart']")
    MESSAGE_TEXT = (By.ID, "messages-text")
    BOOK_IN_CART = (By.XPATH, "//div[@class = 'product-padding product-padding-cart']")
    BOOK_IN_WISH_LIST = (By.XPATH, "//div[@class = 'product-padding product-padding-cart']")
    LOCATION_NAME = (By.CLASS_NAME, "region-location-icon-txt")
    FIELD_FOR_LOCATION_NAME = (By.ID, "region-post")
    FIELD_FOR_COUPONS = (By.XPATH, "//input[@placeholder = 'Купон']")
    SEARCH_FIELD = (By.ID, "search-field")
    SELECTED_LOCATION = (By.XPATH, "//a[@class='a-item']")
    ACTIONS_OF_AUGUST_BLOCK = (By.XPATH, "//div[@class='actions__wrapper' and @data-title = 'Акции августа']/div")
    LABIRINT_LOGO = (By.XPATH, "//a[@class='b-header-b-logo-e-logo-wrap']")
    BOOK_PAGE = (By.XPATH, "//div[@class='product need-watch watched']")
    YOUTH_BOOKS = (By.XPATH, "//a[@href='/genres/3066']")
    REGULAR_PUBLICATIONS = (By.XPATH, "//a[@href='/genres/2137']")
    BUTTON_RAITING = (By.XPATH, "//a[@href='/rating/?id_genre=-1&nrd=1']")
    HTML = (By.TAG_NAME, "html")
    EXCLUSIVE = (By.CSS_SELECTOR, "a[data-event-content = 'Только у нас']")
    PREORDERS = (By.CSS_SELECTOR, "a[data-event-content = 'Предзаказы']")
    CERTIFICATES = (By.CSS_SELECTOR, "a[data-event-content = 'Сертификаты']")
    LITTEST = (By.CSS_SELECTOR, "a[data-event-content = 'Тесты']")
    CONTESTS = (By.CSS_SELECTOR, "a[data-event-content = 'Конкурсы']")
    AGREEMENT = (By.CSS_SELECTOR, "a[data-event-content = 'Пользовательское соглашение']")
    MULTIMEDIA = (By.CSS_SELECTOR, "a[data-event-content = 'CD/DVD']")
    OFFICE = (By.CSS_SELECTOR, "a[data-event-content = 'Канцтовары']")
    SOUVENIRS = (By.CSS_SELECTOR, "a[data-event-content = 'Сувениры']")
    JOURNALS = (By.CSS_SELECTOR, "a[data-event-content = 'Журналы']")
    NEWS = (By.CSS_SELECTOR, "a[data-event-content = 'Новости Л.']")
    ACCEPT_COOKIE = (By.XPATH, "//button[@class='cookie-policy__button js-cookie-policy-agree']")
    BUTTON_COMICS_MANGA = (By.XPATH, "//a[@href='/genres/2993/']")
    TITLE_COMICS = (By.XPATH, "//h1[@class='genre-name']")
    BUTTON_NON_FICTION = (By.XPATH, "//a[@href='/genres/3000/']")
    TITLE_NON_FICTION = (By.XPATH, "//h1[@class='genre-name']")

    def open_main_page(self):
        """
        Open main page.
        """
        self.open_page(self.app.url)

    def open_shopping_cart(self):
        """
        Open shopping cart.
        """
        self.click_element(locator=self.BUTTON_CART)

    def labirint_logo_is_clickacble(self):
        """
        Click logo
        """
        self.click_element(locator=self.BUTTON_CART)
        self.click_element(locator=self.LABIRINT_LOGO)

    def open_wish_list(self):
        """
        Open 'wish list' tab (page).
        """
        self.click_element(locator=self.BUTTON_WISH_LIST)

    def click_button_books(self):
        """
        Open 'books' tab (page).
        """
        self.click_element(locator=self.BUTTON_BOOKS)

    def click_button_best_at_2022(self):
        """
        Open 'Best at 2022' tab (page).
        """
        self.click_element(locator=self.BUTTON_BEST_AT_2022)

    def click_button_club(self):
        """
        Open 'Club' tab (page).
        """
        self.click_element(locator=self.BUTTON_CLUB)

    def click_button_new_books(self):
        """
        Open 'New books' tab (page).
        """
        self.click_element(locator=self.BUTTON_NEW_BOOKS)

    def click_button_maps(self):
        """
        Open 'Maps' tab (page).
        """
        self.click_element(locator=self.BUTTON_MAPS)

    def click_button_support(self):
        """
        Open 'Support' tab (page).
        """
        self.click_element(locator=self.BUTTON_SUPPORT)

    def click_button_raiting(self):
        """
        Open 'Raiting' tab (page).
        """
        self.click_element(locator=self.BUTTON_RAITING)

    def click_button_help(self):
        """
        Open 'Help' tab (page).
        """
        self.click_element(locator=self.BUTTON_HELP)

    def click_button_to_do_order(self):
        """
        Open page for to do order
        """
        self.click_element(locator=self.BUTTON_TO_DO_ORDER)
        time.sleep(2)

    def click_button_to_accept_cookie(self):
        """
        Accept 'Cookies'
        """
        self.click_element(locator=self.ACCEPT_COOKIE)

    def apply_coupon_to_order(self, coupon):
        """
        Apply coupon to order
        """
        self.click_element(locator=self.BUTTON_ADD_COUPONS)
        self.clear(locator=self.FIELD_FOR_COUPONS)
        self.fill(locator=self.FIELD_FOR_COUPONS, value=coupon)
        time.sleep(3)
        self.click_element(locator=self.BUTTON_ACCEPT)
        time.sleep(3)
        elements = self.list_of_all_elements(locator=self.LOCATION_NAME)
        return len(elements)

    def click_button_actions(self):
        """
        Open 'Actions' tab (page).
        """
        self.click_element(locator=self.BUTTON_CLUB)
        self.click_element(locator=self.BUTTON_ACTIONS)

    # def click_button_school(self):
    #     """
    #     Open 'School' tab (page).
    #     """
    #     self.move_to_element(locator=self.BUTTON_ELSE)
    #     time.sleep(3)
    #     self.click_element(locator=self.BUTTON_SCHOOL)

    def click_button_youth_literature(self):
        """
        Open 'Youth literature' tab (page) via dropdown-toggle 'books' on Main page.
        """
        self.move_to_element(locator=self.BUTTON_BOOKS)
        self.click_element(locator=self.YOUTH_BOOKS)

    def click_button_regular_publications(self):
        """
        Open 'Regular publications' tab (page) via dropdown-toggle 'books' on Main page.
        """
        self.move_to_element(locator=self.BUTTON_BOOKS)
        self.click_element(locator=self.REGULAR_PUBLICATIONS)

    def click_button_games(self):
        """
        Open 'Games' tab (page) via dropdown-toggle 'books' on Main page.
        """
        self.move_to_element(locator=self.BUTTON_ELSE)
        time.sleep(5)
        self.click_element(locator=self.BUTTON_GAMES)

    def enter_name_book_and_search(self, name):
        """
        Enter name book in search field and find it
        """
        self.fill(locator=self.SEARCH_FIELD, value=name)
        self.click_element(locator=self.BUTTON_SEARCH)

    def name_of_found_book(self):
        """
        Get name of found book
        """
        element = self.text(locator=self.NAME_BOOK)
        return element

    def find_amount_of_items_in_actions(self):
        """
        Get amount of actions at tab(page) "actions"
        """
        amount = self.list_of_all_elements(locator=self.ACTIONS_OF_AUGUST_BLOCK)
        return len(amount)

    def find_amount_of_videos (self):
        """
        Get amount of videos about the found book
        """
        self.click_element(locator=self.BUTTON_VIDEO)
        amount = self.list_of_all_elements(locator=self.VIDEO_BLOCK)
        return len(amount)

    def find_added_book_in_shopping_card(self):
        """
        Get amount of book in shopping cart
        """
        time.sleep(3)
        self.open_shopping_cart()
        book = self.list_of_all_elements(locator=self.BOOK_IN_CART)
        return len(book)

    def find_added_book_in_wish_list_(self):
        """
        Get amount of book in wish list
        """
        time.sleep(3)
        self.open_wish_list()
        book = self.list_of_all_elements(locator=self.BOOK_IN_WISH_LIST)
        return len(book)

    def change_location_name(self, location):
        """
        Change name of location
        """
        self.click_element(locator=self.LOCATION_NAME)
        self.clear(locator=self.FIELD_FOR_LOCATION_NAME)
        self.fill(locator=self.FIELD_FOR_LOCATION_NAME, value=location)
        self.click_element(locator=self.SELECTED_LOCATION)
        element = self.text(locator=self.LOCATION_NAME)
        return element

    def add_book_in_shopping_cart(self):
        """
        Add book in shopping cart
        """
        self.click_element(locator=self.BUTTON_ADD_IN_CART)

    def add_book_in_cart_through_book_page(self):
        """
        Add book in shopping cart via book page
        """
        self.click_element(locator=self.BUTTON_ADD_IN_CART_ON_BOOK_PAGE)

    def open_any_book_page(self):
        """
        Open some book page
        """
        self.click_element(locator=self.BOOK_PAGE)

    def add_book_in_wish_list(self):
        """
        Add book in wish list
        """
        self.click_element(locator=self.BUTTON_ADD_IN_WISH_LIST)

    def clear_wish_list(self):
        """
        Clear wish list
        """
        self.click_element(locator=self.BUTTON_CLEAR_WISH_LIST)
        self.confirm_action()

    def message_wish_list_is_empty(self):
        """
        Get message "wish list is empty"
        """
        element = self.text(locator=self.MESSAGE_TEXT)
        return element

    def text_from_cart_icon(self):
        """
        Get text from shopping cart icon
        """
        time.sleep(3)
        element = self.text(locator=self.BOOKS_IN_CART_ICON)
        return element

    def text_from_wish_list_icon(self):
        """
        Get text from wish list icon
        """
        time.sleep(3)
        element = self.text(locator=self.BOOKS_IN_WISH_LIST_ICON)
        return element

    # def text_from_youtube_logo_icon(self):
    #     time.sleep(3)
    #     element = self.text(locator=self.YOUTUBE_LOGO)
    #     return element

    def get_location_name(self):
        """
        Get name of location
        """
        element = self.text(locator=self.LOCATION_NAME)
        return element

    def get_relative_link(self):
        """
        Get relative link
        """
        url = urlparse(self.app.driver.current_url)
        return url.path

    def scroll_page_to_end(self):
        """
        Scroll page to end
        """
        self.move_to_end_page(locator=self.HTML)

    def click_button_exclusive(self):
        """
        Open 'exclusive' tab (page) via footer
        """
        self.click_element(locator=self.EXCLUSIVE)

    def click_button_preorders(self):
        """
        Open 'preorders' tab (page) via footer
        """
        self.click_element(locator=self.PREORDERS)

    def click_button_certificates(self):
        """
        Open 'certificates' tab (page) via footer
        """
        self.click_element(locator=self.CERTIFICATES)

    def click_button_littest(self):
        """
        Open 'littest' tab (page) via footer
        """
        self.click_element(locator=self.LITTEST)

    def click_button_contests(self):
        """
        Open 'contests' tab (page) via footer
        """
        self.click_element(locator=self.CONTESTS)

    def click_button_agreement(self):
        """
        Open 'agreement' tab (page) via footer
        """
        self.click_element(locator=self.AGREEMENT)

    def click_button_multimedia(self):
        """
        Open 'multimedia' tab (page) via footer
        """
        self.click_element(locator=self.MULTIMEDIA)

    def click_button_office(self):
        """
        Open 'office' tab (page) via footer
        """
        self.click_element(locator=self.OFFICE)

    def click_button_souvenirs(self):
        """
        Open 'souvenirs' tab (page) via footer
        """
        self.click_element(locator=self.SOUVENIRS)

    def click_button_journals(self):
        """
        Open 'journals' tab (page) via footer
        """
        self.click_element(locator=self.JOURNALS)

    def click_button_news(self):
        """
        Open 'news' tab (page) via footer
        """
        self.click_element(locator=self.NEWS)

    def open_page_comics_and_manga(self):
        """
        Open 'comics, manga' page and get text from title.
        """
        self.click_element(locator=self.BUTTON_BOOKS)
        self.click_element(locator=self.BUTTON_COMICS_MANGA)
        element = self.text(locator=self.TITLE_COMICS)
        return element

    def open_page_non_fiction(self):
        """
        Open 'non-fiction' page and get text from title.
        """
        self.click_element(locator=self.BUTTON_BOOKS)
        self.click_element(locator=self.BUTTON_NON_FICTION)
        time.sleep(2)
        element = self.text(locator=self.TITLE_NON_FICTION)
        return element










