# не работает, упали 2 теста, а нужно чтобы упал второй
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import time

class TestClassName(unittest.TestCase):

    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = check_page(link)
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = check_page(link)
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

def check_page(link):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
    input1.send_keys("Tatyana")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Ivleva")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("edu@test.ru")
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(10)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

              
if __name__ == "__main__":
    unittest.main()