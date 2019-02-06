from selenium.common.exceptions import WebDriverException

from BaseTest import BaseTest
from ListOfProducts import List

from MainPageHeader import Header

from Loginization import Loginization


class TestHeader(BaseTest):

    def test_confirm_location(self):
        """ Confirmation of the default location and verifying the text of the chose location """
        main_page = Header()
        main_page.confirm_default_location()
        assert 'Киев' in main_page.get_loc_text()

    def test_change_location(self):
        """ Choosing the location from the drop down list """
        main_page = Header()
        assert 'ЛЬВОВ' in main_page.choose_location()

    def test_random_location(self):
        """ Choosing random location from the list of location and verifying that popup with changed location is opened"""
        main_page = Header()
        assert main_page.choose_random_loc() is True

    def test_changing_lang(self):
        """ Changing the language of the site from RUS to UKR and verifying the changes """
        main_page = Header()
        main_page.change_language()
        assert 'ua/' in main_page.get_site_url()

    def test_call_back_unsuccessful(self):
        """ Checking the call back with the invalid number and verifying the text of the error """
        main_page = Header()
        assert 'Введите корректный номер' in main_page.call_back_invalid()

    def test_call_back_successful(self):
        """ Checking the call back with the valid number and verifying the text of the success msg"""
        main_page = Header()
        assert 'СПАСИБО ЗА ОБРАЩЕНИЕ!' in main_page.call_back_valid()

    def test_placeholder(self):
        """ Checking presence of the placeholder in the search field """
        main_page = Header()
        assert main_page.is_placeholder_present() is True

    def test_search_results(self):
        """ Testing search results with the valid query"""
        main_page = Header()
        assert main_page.check_search() is True

    def test_invalid_search_results(self):
        """ Testing search results with the invalid query and verifying the text of the error """
        main_page = Header()
        main_page.search_with_invalid_query()
        assert 'Извините, ничего не найдено для "xdcydcyu"' in main_page.get_error_msg_for_query()


    def test_our_products(self):
        """ Checking "Our products" drop down block"""
        main_page = Header()
        assert main_page.our_products() is True

    def test_main_side_menu(self):
        """ Checking the presence of the side drop down menu """
        main_page = Header()
        assert main_page.main_drop_down_menu() is True

    def test_hovering_menu_item(self):
        """ Hovering main menu items"""
        main_page = Header()
        assert main_page.hover_menu_items() is True

    def test_product_block(self):
        """ Checking if the product block is present """
        main_page = Header()
        assert main_page.product_block_is_present() is True

    # def test_product_item_elements(self):
    #     main_page = Header()
    #     assert main_page.check_elements_of_product_item() is True

    def test_linejka_tovarov_block(self):
        """ Checking if the "Linejka tovarov" block is present """
        main_page = Header()
        assert main_page.check_linejka_tovarov() is True

    def test_naboru_block(self):
        """ Checking if the "Naboru" block is present"""
        main_page = Header()
        assert main_page.check_sets() is True

    def test_brands_block(self):
        """ Checking if the "Brands" block is present """
        main_page = Header()
        assert main_page.check_brands_block() is True

    def test_subscribe_unsuccessful(self):
        """ Checking the ability to subscribe for news with the invalid mail and verifying the error msg text """
        main_page = Header()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.subscribe_for_news_unsuccessful()

    def test_subscribe_successful(self):
        """ Checking the ability to subscribe for news with the valid mail and verifying the success msg """
        main_page = Header()
        assert 'Спасибо, что подписались на нашу рассылку.' in main_page.subscribe_for_news_successful()

    def test_stores_tab(self):
        """ Opening the "Stores" tab and verifying that URL is changed"""
        main_page = Header()
        assert '/stockists/' in main_page.check_stores_tab()

    def test_news_tab(self):
        """ Opening the "News" tab and verifying that URL is changed"""
        main_page = Header()
        assert 'novosti' in main_page.check_news_tab()

    def test_help_tab(self):
        """ Opening the 'Help' tab and verifying that popup is appeared"""
        main_page = Header()
        assert main_page.check_help_tab() is True

    def test_certificate_tab(self):
        """ Opening the 'Certificate' tab and verifying that popup is appeared"""
        main_page = Header()
        assert main_page.check_certificate_tab() is True

    def test_wishlist(self):
        """ Opening the 'Wishlist' and verifying that it isn't available for unregistered account """
        main_page = Header()
        assert '#account_login' in main_page.checking_wishlist()

    def test_cart(self):
        """ Opening the 'Cart' and verifying that it isn't available for unregistered account"""
        main_page = Header()
        assert main_page.checking_cart() is True

    def test_logo(self):
        """ Opening the "Uhod" tab, clicking on the logo to verify that it returns to the main page"""
        main_page = Header()
        assert 'https://eva.ua/024/uhod-soboj/' not in main_page.checking_logo()



class TestProductPage(BaseTest):

    def setup(self):
        super(TestProductPage, self).setup()
        self.driver.get(self.base_url+'024-273-293/sredstva-problemnoj-kozhi/')

    def test_list_of_products(self):
        """ Opening the menu category, verifying that url has changed"""
        products_list = List()
        assert '/sredstva-problemnoj-kozhi/' in products_list.open_category()

    def test_filters(self):
        """ Applying filters: county, """
        products_list = List()
        assert products_list.apply_filter_country() is True

    def test_cancellation_of_filter(self):
        """ Cancellation of the filter country"""
        products_list = List()
        # products_list.cancel_filter_country()
        assert products_list.cancel_filter_country() is True


class TestLoginization(BaseTest):

    def test_login(self):
        """ Checking the presence of the pop up after clicking the login btn"""
        main_page = Loginization()
        assert main_page.login() is True

    def test_unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.unsuccessful_authorization_pass()

    def test_unsuccessful_authorization_mail(self):
        """ Checking authorization with the invalid mail and valid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.unsuccessful_authorization_email()

    def test_successful_authorization(self):
        """ Checking authorization with the valid email and password and verifying the name of the account of the
         registered person"""
        main_page = Loginization()
        assert 'Doctor' in main_page.get_account_text()

    def test_recovery_unsucc(self):
        """ Checking recovery of the password with the invalid mail and verifying the text of the error"""
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.recovery_pass_unsuccess()

    def test_recovery_pass(self):
        """ Checking recovery of the password with the valid mail and """
        main_page = Loginization()
        assert 'Если на сайте существует учётная запись с адресом cemmozosyh-0165@yopmail.com,' \
               ' Вы получите письмо со ссылкой для смены пароля.' in main_page.recovery_pass_success()