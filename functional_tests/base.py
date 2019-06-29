import time
import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase as tcs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,\
                                       WebDriverException


MAX_WAIT = 10


class FunctionalTest(tcs):
    def setUp(self):
        self.browser = self.create_chorme()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def create_chorme(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return webdriver.Chrome(chrome_options=options)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def wait_for(self, func):
        time_start = time.time()
        while True:
            try:
                return func()

            except(AssertionError, NoSuchElementException,
                    WebDriverException) as e:
                if time.time() - time_start > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def wait_to_be_logged_in(self, email):
        self.wait_for(
                lambda: self.browser.find_element_by_link_text('Log out'))
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    def wait_to_be_logged_out(self, email):
        self.wait_for(
                lambda: self.browser.find_element_by_name('email'))
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)

