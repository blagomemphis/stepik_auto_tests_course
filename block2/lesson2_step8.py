from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")

    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Ivanov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("Ivanov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    subbtn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    subbtn.click()

finally:
    time.sleep(10)
    browser.quit()
