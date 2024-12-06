Feature: Sauce Demo Checkout

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked
    And the 'Cart' button is clicked
    And the 'Checkout' button is clicked


    Scenario Outline: Incorrect checkout information
      Given the 'First Name' field is filled with '<firstname>'
      And the 'Last Name' field is filled with '<lastname>'
      And the 'Zip Code' field is filled with '<zip>'
      When the 'Continue' button is clicked
      Then the '<error>' checkout message is shown
      Examples:
        | firstname | lastname | zip | error |
        | [blank]   | [blank]  | [blank] | Error: First Name is required |
        | [blank]   | testname | [blank] | Error: First Name is required |
        | [blank]   | [blank]  | 1111111 | Error: First Name is required |
        | testname  | [blank]  | [blank] | Error: Last Name is required |
        | testname  | [blank]  | 1111111 | Error: Last Name is required |
        | testname  | testname | [blank] | Error: Postal Code is required |
        | [blank]   | testname | 11111   | Error: First Name is required |