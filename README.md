# Sauce Demo Automation Testing with Behave

This project uses **Behave** to automate tests for the **Sauce Demo** website..

## Features Tested

- **Login Tests**: Validate correct and incorrect login attempts, including locked-out users and empty fields.
- **Shopping Tests**: Test adding/removing items from the cart and checking out with empty or filled carts.
- **Checkout Tests**: Validate correct error messages when invalid checkout information is provided.

## Project Structure

- **features/**
  - **login.feature**: Contains tests for login functionality.
  - **shopping.feature**: Includes scenarios for shopping actions.
  - **checkout.feature**: Tests for checkout error handling.
  
- **steps/**
  - Step definition files for each feature.

## Requirements

- Python 3.x
- Behave
- Selenium WebDriver
