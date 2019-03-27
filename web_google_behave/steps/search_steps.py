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

from behave import given, when, then
from nose.tools import assert_equals, assert_in
from web_google_behave.pageobjects.google_home import GoogleHomePageObject


@given('the home page is open')
def step_impl(context):
    context.current_page = GoogleHomePageObject()
    context.current_page.open()


# @when('the user logs out')
# def step_impl(context):
#     context.current_page = context.current_page.logout()


# @then('the message "{message}" is shown')
# def step_impl(context, message):
#     assert message in context.current_page.message.get_message()


@then('the title is: {expected_title}')
def step_impl(context, expected_title):
    actual_title = context.current_page.driver.title
    assert_equals(expected_title, actual_title)


@when('the user fill search input with "{search_text}"')
def step_impl(context, search_text):
    context.current_page = context.current_page.fill_search(
        search_text)


@when('the user searches for "{search_text}"')
def step_impl(context, search_text):
    context.execute_steps(
        'When the user searches for "{}" with {}'.format(search_text, 'Search Button'))


@when('the user searches for "{search_text}" with {search_type}')
def step_impl(context, search_text, search_type):
    context.current_page = context.current_page.perform_search(
        search_text, search_type)


@then('every search result contains "{search_text}"')
def step_impl(context, search_text):
    search_results_texts = context.current_page.get_all_search_results_texts()
    for search_result in search_results_texts:
        assert_in(search_text, search_result)


@then('the result in the autocomplete list contains "{search_text}"')
def step_impl(context, search_text):
    assert_in(search_text, context.current_page.get_autocomplete_list_texts())


@then("no results were found")
def step_impl(context):
    for result in ('По запросу', 'ничего не найдено.'):
        assert_in(result, context.current_page.get_search_not_found())


@then("the user click by the first found link")
def step_impl(context):
    context.current_page = context.current_page.open_link()