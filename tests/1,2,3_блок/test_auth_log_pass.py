import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

answer = math.log(int(time.time()))

browser = webdriver.Chrome()
browser.implicitly_wait(30)
link = "https://stepik.org/lesson/236895/step/1"
browser.get(link)
button = browser.find_element(By.XPATH, "/html/body/header/nav/a[2]")
button.click
input = browser.find_element(By.ID, "id_login_email")
input.send_keys("ivleva.smi@yandex.ru")
input = browser.find_element(By.ID, "id_login_password")
input.send_keys("fiona441")
button_in = browser.find_element(By. XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button")
button_in.click

time.sleep(10)
