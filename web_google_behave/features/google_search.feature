Feature: Google search

  Scenario: Open Google home page
    Given the home page is open
     Then the title is: Google

  Scenario: Search with google for "hideo kojima"
    Given the home page is open
     When the user searches for "hideo kojima"
     Then the title is: hideo kojima - Поиск в Google

  Scenario: Search with google for "hideo kojima" with Enter button
    Given the home page is open
    When the user searches for "hideo kojima" with Enter
    Then the title is: hideo kojima - Поиск в Google

  Scenario: Check autocomplete in suggestions inner container for "hideo"
    Given the home page is open
    When the user fill search input with "hideo"
    Then the result in the autocomplete list contains "hideo kojima"

  Scenario: Check autocomplete in suggestions inner container for "hideo kozima"
    Given the home page is open
    When the user fill search input with "hideo kozima"
    Then the result in the autocomplete list contains "hideo kojima"

  Scenario: Search with google for "Python" and check results contains search words
    Given the home page is open
    When the user searches for "Python"
    Then every search result contains "Python"

  Scenario: Searches for google for not existing page and checks results.
    Given the home page is open
    When the user searches for "тфывшфтывфгоцвшофшоцвргругарщфрцашушщоацщуарыаругц" with Enter
    Then no results were found

  Scenario: Search with google for "Python" and open the first found link
    Given the home page is open
    When the user searches for "Python"
    Then the user click by the random found link



