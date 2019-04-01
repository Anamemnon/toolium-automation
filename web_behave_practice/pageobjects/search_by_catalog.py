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

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from web_behave_practice.pageobjects.message import MessagePageObject
from web_behave_practice.pageobjects.secure_area import SecureAreaPageObject


class Search_by_catalog(PageObject):
    def init_page_elements(self):
        self.search_field = InputText(By.ID, 'search_query_top')
        self.search_button = Button(By.NAME, 'submit_search')
        self.categories = Checkboxes(By.CSS_SELECTOR, '#ul_layered_category_0 input')
        self.sizes = Checkboxes(By.CSS_SELECTOR, '#ul_layered_id_attribute_group_1 input')
        self.products_names = Links(By.CSS_SELECTOR, '.product-container .product-name')
        # self.message = MessagePageObject()

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/index.php?id_category=3&controller=category'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.search_field.wait_until_visible()
        return self

# Не работает
    def checkboxes(self, which_checkboxes, elements):
        """ Select checkboxes
            and return
        """

        for checkboxe in self.__dict__[which_checkboxes]:
            checkboxe.checkbox_page_element.check()
            # self.logger.debug("Checkboxe '%s' was selected", checkboxe.web_element.text)
        # return Search_by_catalog(self.driver_wrapper)

    def search_by_search_query(self, query):
        self.search_field.text = query
        self.search_button.click()


    def get_all_products_names(self):
        return [page_element.web_element.text.lower() for page_element in self.products_names.page_elements]