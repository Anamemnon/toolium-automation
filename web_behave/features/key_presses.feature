# Created by chekir at 28.03.2019
Feature: Key presses feature

  Scenario Outline: I want to press any key and see that this key were pressed
    Given the key_presses page is open
    When the key: <key> were pressed
    Then message with text: "<message>" should appear
    Examples:
      | key       | message                 |
      | RETURN    | You entered: ENTER      |
      | SHIFT     | You entered: SHIFT      |
      | SPACE     | You entered: SPACE      |
      | BACKSPACE | You entered: BACK_SPACE |
      | NUMPAD4   | You entered: NUMPAD4    |
      | F7        | You entered: F7         |
