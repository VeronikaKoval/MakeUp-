from base_components.BaseTest import BaseTest

from Pages.MainPageHeader import Header


class TestHeader(BaseTest):

    def setup(self):
        super(TestHeader, self).setup()
        self.driver.get(self.base_url)

    def test_call_back_unsuccessful(self):
        """
        Click on feedback link to get feedback pop up, clicking on the phone field,
        entering invalid phone number, getting text of the error message
        """
        header = Header()
        header.call_back(phone_number='00000000')
        assert 'Введите корректный номер' in header.get_error_text_with_invalid_number(), \
            'The text of the error is absent'

    def test_call_back_successful(self):
        """
        Click on feedback link to get feedback pop up, clicking on the phone field,
        enter valid phone number, getting text of the success message
        """
        header = Header()
        header.call_back(phone_number='123456789')
        assert 'СПАСИБО ЗА ОБРАЩЕНИЕ!' in header.get_successful_msg_text_with_valid_number(), \
            'The success message is absent'

    def test_search_results_block(self):
        """
        Check presence of the search field , click on the search field, enter valid search query "духи"
        and checking whether the block with search results is present
        """
        header = Header()
        assert header.is_search_field_visible() is True, 'The search field is not visible'
        header.enter_query_into_search_field('духи')
        assert header.is_search_result_block_visible() is True, 'The search result block is absent for a valid query'

    def test_invalid_search_results(self):
        """
        Click on the search field, entering invalid search query,
        get text of the error for the invalid query
        """
        header = Header()
        header.enter_query_into_search_field('xdcydcyu')
        assert 'Извините, ничего не найдено для "xdcydcyu"' in header.get_error_msg_for_invalid_query(), \
            'The error message for invalid query is absent'

    def test_open_cart(self):
        """
        Open the 'Cart', verifying that cart popup is opened and it is empty for unregistered account,
        """
        header = Header()
        header.open_cart()
        assert header.is_cart_popup_visible()is True, 'The cart popup is not visible'
        assert 'ВАША КОРЗИНА ПУСТА!' in header.get_text_from_cart_popup(), 'The text in the popup is different'

    def test_logo(self):
        """
        Open the "Uhod" tab, clicking on the logo to verify that it returns to the main page
        """
        header = Header()
        header.click_logo()
        assert header.is_logo_visible() is True, 'Logo is not visible'
        assert 'uhod-soboj/' not in header.get_page_url(), 'URL is different'
