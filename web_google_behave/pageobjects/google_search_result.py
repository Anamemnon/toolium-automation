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


class GoogleSearchResultsPageObject(PageObject):
    def init_page_elements(self):
        self.search_box = InputText(By.NAME, 'q')
        self.search_button = Button(By.XPATH,
                                    '//input[@name="q"]/parent::div/parent::div/parent::div/button')
        self.search_results_texts = Links(By.CSS_SELECTOR, 'div.srg > div.g span.st')
        self.search_results_links = Links(By.CSS_SELECTOR, 'div.srg > div.g div.r > a')
        self.search_not_found = Links(By.CSS_SELECTOR, 'p[role="heading"]')

    def open(self, query):
        """ Open search result url specified in browser

        :returns: this page object instance
        """
        import urllib.parse
        self.driver.get(
            '{}/search?q={}'.format(self.config.get('Test', 'url'), urllib.parse.quote(query)))
        return self

    def wait_until_loaded(self):
        """ Wait until page is loaded

        :returns: this page object instance
        """
        self.search_box.wait_until_visible()
        return self

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

    def get_all_search_results_texts(self):
        """ Gets all search results texts from search results page

        :returns: texts that search results contains
        """
        return [search_result.web_element.text for search_result in
                self.search_results_texts.page_elements]

    def get_all_search_results_links(self):
        """ Gets all search results links from search results page

        :returns: texts that search results contains
        """
        return [search_result.web_element for search_result in
                self.search_results_links.page_elements]

    def get_search_not_found(self):
        return self.search_not_found.page_elements.pop(0).web_element.text

    def open_link(self):
        import random
        random.choice(self.get_all_search_results_links()).click()
        return GoogleSearchResultsPageObject(self.driver_wrapper)
