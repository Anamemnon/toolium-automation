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


class MessagePageObject(PageObject):
    def init_page_elements(self):
        self.message = Text(By.CSS_SELECTOR, 'div.alert li')
        self.successful_message = Text(By.CSS_SELECTOR, '.page-heading')
        self.logout_message = Text(By.CSS_SELECTOR, '#login_form .page-subheading')

    def get_fail_login_message(self):
        """ Get first line of actual message

        :returns: str with message
        """
        return self.message.wait_until_visible(2).text

    def get_success_login_message(self):
        return self.successful_message.wait_until_visible(2).text

    def get_logout_message(self):
        return self.logout_message.wait_until_visible(2).text
