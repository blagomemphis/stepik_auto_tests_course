from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    n1 = num1.text

    num2 = browser.find_element(By.ID, "num2")
    n2 = num2.text

    sum = int(n1) + int(n2)

    select = Select(browser.find_element(By.ID,"dropdown"))
    select.select_by_value(str(sum))

    subbtn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    subbtn.click()

finally:
    time.sleep(10)
    browser.quit()

