from constants import LoginMessages
from constants import MainPageMessages
from selenium.common.exceptions import TimeoutException


class TestLoginPage:

    def test_valid_login(self, app):
        """
        Valid log in.
        """
        app.login_page.open_login_page()
        username = LoginMessages.LOGIN
        password = LoginMessages.PASSWORD
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.get_relative_link() == '/cabinet/'

    def test_login_with_only_invalid_code(self, app):
        """
        Log in using only invalid code
        """
        app.login_page.open_login_page()
        username = 'CA9C-4B90-B488'
        app.login_page.entry_invalid_code(username=username)
        assert app.login_page.text_error_invalid_data() == LoginMessages.ERROR_INVALID_CODE

    def test_login_with_valid_email_and_invalid_code(self, app):
        """
        Invalid log in with invalid data.
        """
        app.login_page.open_login_page()
        username = LoginMessages.LOGIN
        password = 'CA9C-4B90-B489'
        app.login_page.entry_valid_email_and_invalid_code(username=username, password=password)
        assert app.login_page.text_error_invalid_data() == LoginMessages.ERROR_INVALID_CODE

    def test_empty_username(self, app):
        """
        Empty username.
        """
        app.login_page.open_login_page()
        username = None
        try:
            app.login_page.entry_invalid_code(username=username)
        except TimeoutException as e:
            return e

    def test_open_tab_coupons(self, app, my_cabinet):
        """
        Opening 'coupons' tab via my cabinet page.
        """
        app.login_page.open_tab_coupons()
        assert app.login_page.get_relative_link() == '/cabinet/coupons/'

    def test_there_are_coupons(self, app, my_cabinet):
        """
        There is at least one coupon in my cabinet (tab coupons)
        """
        assert app.login_page.find_amount_of_coupons() > 0

    def test_there_are_not_orders(self, app, my_cabinet):
        """
        There are no orders in my cabinet
        """
        assert app.login_page.text_no_orders() == LoginMessages.TEXT_NO_ORDERS

    def test_wish_list_is_not_empty(self, app, my_cabinet):
        """
        There is at least one book in wish list
        """
        assert app.login_page.find_amount_of_wish_list_items() > 0


    def test_open_tab_viewing_history(self, app, my_cabinet):
        """
        Opening viewing history tab via my cabinet page.
        """
        app.login_page.open_tab_viewing_history()
        assert app.login_page.get_relative_link() == '/cabinet/'

    def test_there_is_items_of_viewing_history(self, app, my_cabinet):
        """
        There is at least one book in viewing history
        """
        assert app.login_page.find_amount_of_items_in_viewing_history() > 0

    def test_open_tab_personal_data(self, app, my_cabinet):
        """
        Opening 'personal data' tab via my cabinet page.
        """
        app.login_page.open_tab_personal_data()
        assert app.login_page.get_relative_link() == '/cabinet/personal/'

    def test_open_tab_settings(self, app, my_cabinet):
        """
        Opening 'setting' tab via my cabinet page.
        """
        app.login_page.open_tab_settings()
        assert app.login_page.get_relative_link() == '/cabinet/settings/'

    def test_there_are_subscriptions(self, app, my_cabinet):
        """
        There is at least one subscription in my cabinet
        """
        assert app.login_page.find_amount_of_subscriptions() > 0

    def test_there_are_recommendations(self, app, my_cabinet):
        """
        There is at least one recommendation in my cabinet
         """
        assert app.login_page.find_amount_of_recommendations() > 0

    def test_to_apply_coupon_to_order(self, app, my_cabinet):
        """
        Applying a coupon to an order
        """
        app.main_page.open_shopping_cart()
        app.main_page.click_button_to_do_order()
        coupon = 'BOJ80UMER6'
        try:
            assert app.main_page.apply_coupon_to_order(coupon=coupon) == 1
        except TimeoutException as coupon_have_already_accepted:
            return coupon_have_already_accepted


class TestMainPage:

    def test_open_tab_books(self, app):
        """
        Opening 'books' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_books()
        assert app.main_page.get_relative_link() == '/books/'

    def test_labirint_logo_is_clickable_and_lead_to_main_page(self, app):
        """
        Logo on is clickable and lead to main page
        """
        app.main_page.open_main_page()
        app.main_page.labirint_logo_is_clickacble()
        assert app.main_page.get_relative_link() == '/'

    def test_open_tab_best(self, app):
        """
        Opening 'best' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_best_at_2022()
        assert app.main_page.get_relative_link() == '/best/'

    def test_open_tab_club(self, app):
        """
        Opening 'club' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_club()
        assert app.main_page.get_relative_link() == '/club/'

    def test_open_tab_new_books(self, app):
        """
        Opening 'new books' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_new_books()
        assert app.main_page.get_relative_link() == '/novelty/'

    def test_open_shopping_cart(self, app):
        """
        Opening 'shopping cart' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.open_shopping_cart()
        assert app.main_page.get_relative_link() == '/cart/'

    def test_open_tab_support(self, app):
        """
        Opening 'support' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_support()
        assert app.main_page.get_relative_link() == '/support/'

    def test_open_tab_rating(self, app):
        """
        Opening 'rating' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_raiting()
        assert app.main_page.get_relative_link() == '/rating/'

    def test_open_tab_maps(self, app):
        """
        Opening 'maps' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_maps()
        assert app.main_page.get_relative_link() == '/maps/'

    def test_open_tab_help(self, app):
        """
        Opening 'help' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_help()
        assert app.main_page.get_relative_link() == '/help/'

    def test_check_that_location_is_saint_petersburg(self, app):
        """
        Location is set Saint-Petersburg
        """
        app.main_page.open_main_page()
        assert app.main_page.get_location_name() == LoginMessages.LOCATION_NAME

    def test_change_location_name(self, app):
        """
        To set location 'Благовещенск"
        """
        app.main_page.open_main_page()
        location = 'Благовещенск'
        assert app.main_page.change_location_name(location=location) == location

    def test_there_are_actions_in_august(self, app):
        """
        There is at least one action in August
        """
        app.main_page.open_main_page()
        app.main_page.click_button_actions()
        assert app.main_page.find_amount_of_items_in_actions() > 0

    def test_find_book_through_the_search_bar(self, app):
        """
        Search book via the search bar
        """
        app.main_page.open_main_page()
        name = 'Маленький принц'
        app.main_page.enter_name_book_and_search(name=name)
        assert app.main_page.name_of_found_book() == name

    def test_find_video_about_book_through_the_search_bar(self, app):
        """
        Search video about founded book
        """
        app.main_page.open_main_page()
        name = 'Маленький принц'
        app.main_page.enter_name_book_and_search(name=name)
        assert app.main_page.find_amount_of_videos() > 0

    def test_add_book_in_shopping_cart(self, app):
        """
        Add book in shopping cart
        """
        app.main_page.open_main_page()
        app.main_page.add_book_in_shopping_cart()
        assert app.main_page.find_added_book_in_shopping_card() == 1

    def test_open_any_book_page(self, app):
        """
        Open some book page
        """
        app.main_page.open_main_page()
        app.main_page.open_any_book_page()
        assert app.main_page.get_relative_link() != '/'

    def test_add_book_in_cart_through_book_page(self, app):
        """
        Add book in shopping cart via book page
        """
        app.main_page.open_main_page()
        app.main_page.open_any_book_page()
        app.main_page.add_book_in_cart_through_book_page()
        assert app.main_page.find_added_book_in_shopping_card() == 1

    def test_open_tab_youth_literature(self, app):
        """
        Opening 'youth literature' tab on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_youth_literature()
        assert app.main_page.get_relative_link() == '/genres/3066/'

    def test_open_order_page(self, app):
        """
        Open order page via shopping cart
        """
        app.main_page.open_main_page()
        app.main_page.click_button_to_accept_cookie()
        app.main_page.add_book_in_shopping_cart()
        assert app.main_page.find_added_book_in_shopping_card() == 1
        app.main_page.click_button_to_do_order()
        assert app.main_page.get_relative_link() == '/basket/checkout/'

    def test_check_amount_of_book_in_cart_icon(self, app):
        """
        Checking amount of book in shopping cart icon
        """
        app.main_page.open_main_page()
        app.main_page.add_book_in_shopping_cart()
        assert app.main_page.text_from_cart_icon() == '1'

    def test_add_book_in_wish_list(self, app):
        """
        Adding book in wish list
        """
        app.main_page.open_main_page()
        app.main_page.add_book_in_wish_list()
        assert app.main_page.find_added_book_in_wish_list_() == 1

    def test_check_amount_of_book_in_wish_list_icon(self, app):
        """
        Checking amount of book in wish list icon
        """
        app.main_page.open_main_page()
        app.main_page.add_book_in_wish_list()
        assert app.main_page.text_from_wish_list_icon() == '1'

    def test_delete_books_in_wish_list(self, app):
        """
        Removal book from wish list
        """
        app.main_page.open_main_page()
        app.main_page.add_book_in_wish_list()
        assert app.main_page.find_added_book_in_wish_list_() == 1
        app.main_page.clear_wish_list()
        assert app.main_page.message_wish_list_is_empty() == MainPageMessages.WISH_LIST_IS_EMPTY

    def test_open_tab_comics_and_manga(self, app):
        """
        Opening 'comics, manga' tab via books page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_to_accept_cookie()
        assert app.main_page.open_page_comics_and_manga() == MainPageMessages.TITLE_COMICS_MANGA

    def test_open_tab_non_fiction(self, app):
        """
        Opening 'non-fiction' tab via books page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_to_accept_cookie()
        assert app.main_page.open_page_non_fiction() == MainPageMessages.TITLE_NON_FICTION


class TestFooter:

    def test_open_exclusive_page(self, app):
        """
        Opening 'exclusive' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_to_accept_cookie()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_exclusive()
        assert app.main_page.get_relative_link() == '/top/exclusive/'

    def test_open_certificates_page(self, app):
        """
        Opening 'certificates' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_certificates()
        assert app.main_page.get_relative_link() == '/top/certificates/'

    def test_open_littest_page(self, app):
        """
        Opening 'littest' page via footer on main page.
         """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_littest()
        assert app.main_page.get_relative_link() == '/littest/'

    def test_open_contests_page(self, app):
        """
        Opening 'contests' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_contests()
        assert app.main_page.get_relative_link() == '/contests/'

    def test_open_agreement_page(self, app):
        """
        Opening 'agreement' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_agreement()
        assert app.main_page.get_relative_link() == '/agreement/'

    def test_open_multimedia_page(self, app):
        """
        Opening 'multimedia' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_multimedia()
        assert app.main_page.get_relative_link() == '/multimedia/'

    def test_open_office_page(self, app):
        """
        Opening 'office' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_office()
        assert app.main_page.get_relative_link() == '/office/'

    def test_open_souvenirs_page(self, app):
        """
        Opening 'souvenirs' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_souvenirs()
        assert app.main_page.get_relative_link() == '/souvenir/'

    def test_open_journals_page(self, app):
        """
        Opening 'journals' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_journals()
        assert app.main_page.get_relative_link() == '/journals/'

    def test_open_news_page(self, app):
        """
        Opening 'news' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_news()
        assert app.main_page.get_relative_link() == '/news/'

    def test_open_preorders_page(self, app):
        """
        Opening 'preorders' page via footer on main page.
        """
        app.main_page.open_main_page()
        app.main_page.click_button_to_accept_cookie()
        app.main_page.scroll_page_to_end()
        app.main_page.click_button_preorders()
        assert app.main_page.get_relative_link() == '/top/skoro-v-prodazhe/'
