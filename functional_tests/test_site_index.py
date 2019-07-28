from .base import FunctionalTest
import time
TEST_PAGE = '../docs/md_pages/my_blog_design.md'


class NewListPageTest(FunctionalTest):

    def test_open_index_page(self):
        # open home page, title with qicai21
        self.browser.get(self.live_server_url)
        self.assertIn('qicai21', self.browser.title)

        # a top bar lay on the top
        top_bar = self.browser.find_element_by_id('top_bar')
        # Menu button in the center of bar, they are blog, media, laboratory
        buttons = top_bar.find_elements_by_tag_name('a')
        self.assertEqual(len(buttons), 7)
        # two tools button in the right, managing and sharing
        self.browser.find_element_by_id('manage_btn')
        self.browser.find_element_by_id('share_btn')

        # and main page's is showing a "welcome to view this website!" header
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header, 'Welcome to view this website!')

        # click super-list button, the page trans to super-list page
        self.browser.find_element_by_id('ref_to_lists').click()
        self.assertEqual(self.browser.title, 'To-Do lists')

        # click blog button, the page trans to blog index page,
        self.browser.find_element_by_id('ref_to_blogs').click()

        # a side label of toc on the left
        toc_lab = self.browser.find_element_by_id('toc')
        # click the first link on left toc, main page trans to the relative
        toc_lab.find_elements_by_xpath('ul[@class="sectlevel1"]/li/a')[0].click()
        # page, and showing the same content-header with the left link
        text_1 = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(text_1, 'A simple Text')

        # when you click another link on the left, main page trans too.

        # click home-link, page back to blog welcome page.

        # click manage button, notificating a "manage link already send to admin's email"
        # admin can upload new md doc
        # admin can delete exist md doc by email authentication
