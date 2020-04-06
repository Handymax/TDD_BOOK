import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase as tcs
from selenium import webdriver


class NewVisitorTest(tcs):

    def setUp(self):
        self.browser = self.create_chorme()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def create_chorme(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return webdriver.Chrome(chrom_options=options)

