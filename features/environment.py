import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.homepage import Homepage


def get_driver():
    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")
    service = ChromeService(chromedriver_path)
    return webdriver.Chrome(service=service)


def before_all(context):
    context.homepage = Homepage(get_driver())


def after_all(context):
    context.homepage.close_page()