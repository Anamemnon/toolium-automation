# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

from web_google_behave.pageobjects.google_search_result import GoogleSearchResultsPageObject


class GoogleHomePageObject(PageObject):
    def init_page_elements(self):
        self.search_box = InputText(By.NAME, 'q')
        self.search_button = Button(By.NAME, 'btnK')
        # self.autocomplete_list = Links(By.XPATH, "//ul/li/span")
        self.autocomplete_list_texts = Links(By.XPATH, "//ul/li/*/*/*/span")

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.search_box.wait_until_visible()
        return self

    def fill_search(self, search_text):
        """ Fill search input form and submit it

        :param search_text: str
        :returns: search_result_page object instance
        """
        self.logger.debug("Writing in search input: '%s'", search_text)
        self.search_box.text = search_text

        return GoogleHomePageObject(self.driver_wrapper)

    def perform_search(self, search_text, by_button='Search Button'):
        """ Fill search input form and submit it

        :param search_text: str
        :returns: search_result_page object instance
        """
        self.logger.debug("Performing search for '%s'", search_text)
        self.search_box.text = search_text

        if by_button == 'Search Button':
            self.search_button.click()
        elif by_button == 'Enter':
            self.search_box.text = Keys.RETURN

        return GoogleSearchResultsPageObject(self.driver_wrapper)

    def get_autocomplete_list_texts(self):
        return [search_result.web_element.text for search_result in
                self.autocomplete_list_texts.page_elements]