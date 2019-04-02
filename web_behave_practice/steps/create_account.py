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

from behave import given, when, then, step
from nose.tools import assert_equal


@when('the user create a email: "{email}"')
def step_impl(context, email):
    user = {'email': email, 'password': None}
    context.current_page = context.current_page.create_email(user)


@then("the create account page is open")
def step_impl(context):
    # context.current_page = CreateAccountPageObject()
    context.current_page.open()
    context.current_page.wait_until_loaded()


@given("the user select gender {gender}.")
def step_impl(context, gender):
    context.current_page.select_gender(gender)


@step('enters the first name "{first_name}" and the last name "{last_name}"')
def step_impl(context, first_name, last_name):
    context.current_page.enter_names(first_name, last_name)


@step("enter the day of birth: {day}.{month}.{year}")
def step_impl(context, day, month, year):
    date = day.lstrip('0'), month.lstrip('0'), year.lstrip('0')
    context.current_page.enter_date_of_birth(date)