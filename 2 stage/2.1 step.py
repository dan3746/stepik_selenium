import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def find(element):
  browser.execute_script('return arguments[0].scrollIntoView(true);', element)


browser = webdriver.Chrome()
link = " http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = int(browser.find_element(By.ID, "input_value").text)


option1 = browser.find_element(By.ID, "answer")
find(option1)
option1.send_keys(calc(x_element))


option2 = browser.find_element(By.ID, "robotCheckbox")
find(option2)
option2.click()

option3 = browser.find_element(By.ID, "robotsRule")
find(option3)
option3.click()

button = browser.find_element(By.TAG_NAME, 'button')
find(button)
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


