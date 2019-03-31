Feature: Login

  Scenario: invalid email address
    Given the home page is open
     When the user logs in with email "123" and password "321"
     Then the message "Invalid email address." is shown

  Scenario: invalid password
    Given the home page is open
    When the user logs in with email "chekirdv@yandex.ru" and password "321"
    Then the message "Invalid password." is shown

  Scenario: successful login
    Given the home page is open
    When the user logs in with email "chekirdv@yandex.ru" and password "@t^u8&mpa"
    Then the successful message "MY ACCOUNT" is shown

  Scenario: successful logout
    Given the home page is open
     When the user logs in with email "chekirdv@yandex.ru" and password "@t^u8&mpa"
      And the user logs out
     Then the logout message "ALREADY REGISTERED?" is shown
