from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidentally tries to submit
        # an empty list item. she hits ENTER on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # the browser intercepts the request, and does not load the
        # list page
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # she starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))

        # and she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for(
                lambda: self.check_for_row_in_list_table('1: buy milk')
                )

        # perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # again, the browser will not comply
        self.wait_for(
                lambda: self.check_for_row_in_list_table('1: buy milk')
                )
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
                '#id_text:invalid'
        ))

        # and she can correct it by filling some text in
        self.get_item_input_box().send_keys('make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
                '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for(
                lambda: self.check_for_row_in_list_table('1: buy milk')
        )
        self.wait_for(
                lambda: self.check_for_row_in_list_table('2: make tea')
        )

    def test_cannot_add_duplicate_items(self):
        # edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for(
                lambda: self.check_for_row_in_list_table('1: buy wellies')
        )

        # she accidentally tries to ENTER a duplicate item
        self.get_item_input_box().send_keys('buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # she sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You've already got this in your list"
        ))
