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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class KeyPressesPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.ID, 'username')
        self.container = InputText(By.CLASS_NAME, 'example')
        self.message = Text(By.ID, 'result')

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/key_presses'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self, timeout=0):
        """ Wait until key presses page is loaded

        :returns: this page object instance
        """
        self.container.wait_until_visible()
        return self

    def send_key(self, key):
        key = getattr(Keys, key)
        ActionChains(self.driver).send_keys(key).perform()

    def get_message(self):
        return self.message.text
