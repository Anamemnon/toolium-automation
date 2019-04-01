# Created by chekir at 31.03.2019
Feature: search by the catalog

#  Scenario Outline: Search by categories
#    Given the catalog page is open
#    When the user selects categories: <categories>
#    Examples:
#      | categories    |
#      | Tops          |
##      | Dresses       |
##      | Tops, Dresses |

  Scenario Outline: Search using search field
    Given the catalog page is open
    When the user enters a search query: <query>
    Then each of the found product is <query>
    Examples:
      | query         |
      | shirt         |
      | printed dress |
