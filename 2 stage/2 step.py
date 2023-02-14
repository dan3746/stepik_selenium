import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')





x_element = int(browser.find_element(By.ID, "num1").text)
y_element = int(browser.find_element(By.ID, "num2").text)

sum = x_element + y_element

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(f"{sum}") # ищем элемент с текстом "Python"

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


