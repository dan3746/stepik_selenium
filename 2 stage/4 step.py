import time

from selenium import webdriver
from selenium.webdriver.common.by import By



try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

