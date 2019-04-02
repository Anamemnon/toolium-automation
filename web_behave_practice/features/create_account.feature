Feature: Create an account

  Background: open the page for account creation
    Given the home page is open
    When the user create a email: "g@mail.ru"
    Then the create account page is open

  Scenario: fill your personal information
    Given the user select gender Mr.
    And enters the first name "Vinni" and the last name "Puh"
    And enter the day of birth: 27.05.1994