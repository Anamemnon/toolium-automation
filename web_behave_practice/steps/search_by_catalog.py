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
from nose.tools import assert_in
from web_behave_practice.pageobjects.search_by_catalog import Search_by_catalog


@given('the catalog page is open')
def step_impl(context):
    context.current_page = Search_by_catalog()
    context.current_page.open()


@when("the user selects categories: <{categories}>")
def step_impl(context, categories):
    categories = categories.split(', ')
    context.current_page = context.current_page.checkboxes('categories', categories)
    # context.current_page.checkboxes('categories', categories)


@when("the user enters a search query: {query}")
def step_impl(context, query):
    context.current_page.search_by_search_query(query)


@then("each of the found product is {query}")
def step_impl(context, query):
    for product_name in context.current_page.get_all_products_names():
        if not isinstance(query, list):
            query = query.split()
        for q in query:
            assert_in(q, product_name)