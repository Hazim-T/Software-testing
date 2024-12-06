Feature: Sauce Demo Shopping

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked


    Scenario: Empty cart checkout
      Given the 'Cart' button is clicked
      And the 'Checkout' button is clicked
      And the 'First Name' field is filled with 'testname_first'
      And the 'Last Name' field is filled with 'testname_last'
      And the 'Zip Code' field is filled with '1111'
      When the 'Continue' button is clicked
      Then the price should read 'Total: $0.00'
      ## to reset the cart
      And the 'Finish' button is clicked
      And the 'Back' button is clicked

      
    Scenario: Buying a Onesie
      Given the 'Sauce Labs Onesie' is added to the cart
      And the 'Cart' button is clicked
      And the 'Checkout' button is clicked
      And the 'First Name' field is filled with 'testname_first'
      And the 'Last Name' field is filled with 'testname_last'
      And the 'Zip Code' field is filled with '1111'
      When the 'Continue' button is clicked
      Then the price should read 'Total: $8.63'
      ## to reset the cart
      And the 'Finish' button is clicked
      And the 'Back' button is clicked


    Scenario: Buying a both T-shirts
      Given the 'Sauce Labs Bolt T-Shirt' is added to the cart
      And the 'Test.allTheThings() T-Shirt (Red)' is added to the cart
      And the 'Cart' button is clicked
      And the 'Checkout' button is clicked
      And the 'First Name' field is filled with 'testname_first'
      And the 'Last Name' field is filled with 'testname_last'
      And the 'Zip Code' field is filled with '1111'
      When the 'Continue' button is clicked
      Then the price should read 'Total: $34.54'
      ## to reset the cart
      And the 'Finish' button is clicked
      And the 'Back' button is clicked


    Scenario: Buying all items
      Given the 'Sauce Labs Onesie' is added to the cart
      And the 'Sauce Labs Bolt T-Shirt' is added to the cart
      And the 'Test.allTheThings() T-Shirt (Red)' is added to the cart
      And the 'Sauce Labs Backpack' is added to the cart
      And the 'Sauce Labs Fleece Jacket' is added to the cart
      And the 'Sauce Labs Bike Light' is added to the cart
      And the 'Cart' button is clicked
      And the 'Checkout' button is clicked
      And the 'First Name' field is filled with 'testname_first'
      And the 'Last Name' field is filled with 'testname_last'
      And the 'Zip Code' field is filled with '1111'
      When the 'Continue' button is clicked
      Then the price should read 'Total: $140.34'
      ## to reset the cart
      And the 'Finish' button is clicked
      And the 'Back' button is clicked


    Scenario Outline: Adding and removing items from cart
      Given the '<item>' is added to the cart
      And the 'Cart' button is clicked
      When the '<item>' is removed from the cart
      Then the cart should be empty
      Examples:
        | item |
        | Sauce Labs Onesie |
        | Sauce Labs Bolt T-Shirt |
        | Test.allTheThings() T-Shirt (Red) |
        | Sauce Labs Backpack |
        | Sauce Labs Fleece Jacket |
        | Sauce Labs Bike Light |