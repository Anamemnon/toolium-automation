Feature: Create an account

  Scenario: create e-mail
    Given the home page is open
    When the user create a email: "g@mail.ru"
    Then the create account page is open

#  Scenario: fill your personal information
#    Given the create account page is open
