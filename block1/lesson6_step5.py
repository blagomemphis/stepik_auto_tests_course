from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')

    browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()

    browser.find_element(By.TAG_NAME, 'input').send_keys("Ivan")
    browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, 'city').send_keys("Smolensk")
    browser.find_element(By.ID, 'country').send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()