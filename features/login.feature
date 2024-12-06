Feature: Sauce Demo Login Test

  Background:
    Given the home page is opened


    Scenario Outline: Incorrect login attempts
      Given the 'Username' field is filled with '<username>'
      And the 'Password' field is filled with '<password>'
      When the 'Login' button is clicked
      Then the '<errorMessage>' message is shown
      Examples:
        | username        | password       | errorMessage                                                              |
        | [blank]         | [blank]        | Epic sadface: Username is required                                        |
        | standard_user   | [blank]        | Epic sadface: Password is required                                        |
        | standard_user   | wrong_password | Epic sadface: Username and password do not match any user in this service |
        | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.                       |


    Scenario Outline: Successful login
      Given the 'Username' field is filled with '<username>'
      And the 'Password' field is filled with '<password>'
      When the 'Login' button is clicked
      Then the 'Products' page is opened
      Examples:
        | username      | password     |
        | standard_user | secret_sauce |
        | problem_user  | secret_sauce |
        | performance_glitch_user | secret_sauce |


    Scenario Outline: Successful logout
      Given the 'Username' field is filled with '<username>'
      And the 'Password' field is filled with '<password>'
      And the 'Login' button is clicked
      And the 'Options' button is clicked
      When the 'Logout' button is clicked
      Then the 'Login' page is opened
      Examples:
        | username      | password     |
        | standard_user | secret_sauce |
        | problem_user  | secret_sauce |
        | performance_glitch_user | secret_sauce |