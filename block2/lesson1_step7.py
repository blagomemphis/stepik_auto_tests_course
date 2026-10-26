from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    t = treasure.get_attribute("valuex")
    x = calc(t)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(x)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    subbtn = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    subbtn.click()

finally:
    time.sleep(10)
    browser.quit()
