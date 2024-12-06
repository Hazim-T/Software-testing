from operator import concat

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    PAGE_URL = "https://www.saucedemo.com/"

    text_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password"),
        "First Name": (By.ID, "first-name"),
        "Last Name": (By.ID, "last-name"),
        "Zip Code": (By.ID, "postal-code")
    }

    messages = {
        "login error": (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3"),
        "checkout error": (By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error > h3"),
        "price label": (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")
    }

    navigation_buttons = {
        "Login": (By.ID, "login-button"),
        "Cart": (By.CLASS_NAME, "shopping_cart_link"),
        "Options": (By.ID, "react-burger-menu-btn"),
        "Logout": (By.ID, "logout_sidebar_link"),
        "Reset": (By.ID, "reset_sidebar_link"),
        "Close": (By.ID, "react-burger-cross-btn"),
        "Checkout": (By.ID, "checkout"),
        "Continue": (By.ID, "continue"),
        "Finish": (By.ID, "finish"),
        "Back": (By.ID, "back-to-products")
    }

    pages = {
        "Login" : PAGE_URL,
        "Products": concat(PAGE_URL, "inventory.html"),
        "Cart": concat(PAGE_URL, "cart.html"),
        "Checkout": concat(PAGE_URL, "checkout-step-one.html"),
        "Final": concat(PAGE_URL, "checkout-complete.html")
    }

    products = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    }

    remove_products = {
        "Sauce Labs Backpack": (By.ID, "remove-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "remove-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "remove-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "remove-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "remove-sauce-labs-onesie"),
        "Test.allTheThings() T-Shirt (Red)": (By.ID, "remove-test.allthethings()-t-shirt-(red)")
    }

    cart_items = (By.CSS_SELECTOR, "#item_0_title_link > div")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def close_page(self):
        self.driver.quit()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def click_button(self, button):
        # Element not interactable because some buttons are not fully loaded when trying to press them
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.navigation_buttons[button])
        )

        if button == "Options":
            self.driver.find_element(*self.navigation_buttons[button]).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
            )
        elif button == "Close":
            self.driver.find_element(*self.navigation_buttons[button]).click()
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.CLASS_NAME, "bm-menu"))
            )
        else:
            self.driver.find_element(*self.navigation_buttons[button]).click()

    def get_error_message(self, message):
        return self.driver.find_element(*self.messages[message]).text

    def get_checkout_error_message(self):
        return self.driver.find_element(*self.messages["checkout error"]).text

    def login(self, username, password):
        self.fill_out_field("Username", username)
        self.fill_out_field("Password", password)
        self.click_button("Login")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.products[product_name]).click()


    def remove_product_from_cart(self, product_name):
        self.driver.find_element(*self.remove_products[product_name]).click()

    def go_to_cart(self):
        self.click_button("Cart")

    def proceed_to_checkout(self):
        self.click_button("Checkout")

    def get_total(self):
        return self.driver.find_element(*self.messages["price label"]).text

    def get_current_url(self):
        return self.driver.current_url

    def is_cart_empty(self):
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
        return len (cart_items) == 0