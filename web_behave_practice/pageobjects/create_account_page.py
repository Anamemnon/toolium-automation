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


class CreateAccountPageObject(PageObject):
    def init_page_elements(self):
        self.customer_firstname = InputText(By.ID, 'customer_firstname')

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}?controller=authentication&back=my-account#account-creation'.format(
            self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.customer_firstname.wait_until_visible()
        return self


    # def create_email(self, user):
    #     self.logger.debug("Create email '%s'", user['email'])
    #     self.email.text = user['email']
    #     self.email_create_button.click()
    #     return CreateAccountPageObject(self.driver_wrapper)
