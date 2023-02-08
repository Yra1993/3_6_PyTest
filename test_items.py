import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_card_btn(browser):
        browser.get(link)
        time.sleep(10)
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button is not None, "button not found"
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()