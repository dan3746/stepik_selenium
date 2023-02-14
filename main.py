import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    global action
    action = ActionChains(driver)

    driver.get('https://stage.dircont.com/signin')
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
            )
    yield

    driver.quit()

def correct_enter(user_data):
    driver.find_element(By.NAME, 'email').send_keys(user_data['email'])
    driver.find_element(By.NAME, 'password').send_keys(user_data['password'])
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/ng-component/div/div[1]/app-left-menu/ul/li[8]'))
    )
    element.click()

tool_bar_dict = {
    "Создать папку": "//app-file-manager-toolbar/div[1]/div[1]/app-svg-icon",
    "Вырезать": "//app-file-manager-toolbar/div[1]/div[2]/app-svg-icon",
    "Копировать": "//app-file-manager-toolbar/div[1]/div[3]/app-svg-icon",
    "Вставить": "//app-file-manager-toolbar/div[1]/div[4]/app-svg-icon",
    "Переименовать": "//app-file-manager-toolbar/div[1]/div[5]/app-svg-icon",
    "Загрузить с компьютера": "//app-file-manager-toolbar/div[1]/div[6]/app-svg-icon",
    "Скачать": "//app-file-manager-toolbar/div[1]/div[7]/app-svg-icon",
    "Архив": "//app-file-manager-toolbar/div[1]/div[8]/app-svg-icon",
    "Управление совместным доступом": "//app-file-manager-toolbar/div[1]/div[9]/app-svg-icon",
    "Удалить": "//app-file-manager-toolbar/div[1]/div[10]/app-svg-icon",
    "Назад": "//app-file-manager-toolbar/div[2]/div[1]/app-svg-icon",
    "Вперед": "//app-file-manager-toolbar/div[2]/div[2]/app-svg-icon",
    "Вид списком": "//app-file-manager-toolbar/div[2]/div[3]/app-svg-icon",
    "Вид плиткой": "//app-file-manager-toolbar/div[2]/div[3]/app-svg-icon",
    "Справка": "//app-file-manager-toolbar/div[2]/div[4]/app-svg-icon"
}

UserDataAP1 = {'email': 'base_admin_of_user@example.com', 'password': '123', 'name': 'Gonzalez Н.J.'}

class TestSteps:
    def test_step_2(self):
        print("\n")
        correct_enter(UserDataAP1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tool_bar_dict["Создать папку"]))
        )

        for button in tool_bar_dict:
            action.move_to_element(driver.find_element(
                By.XPATH, tool_bar_dict[button])
            )
            action.perform()
            time.sleep(0.1)
            assert driver.find_element(By.CLASS_NAME, "tooltip-inner").text == button
            print('Проверена подсказка для кнопки: ', button)
            if button == "Вид списком":
                driver.find_element(By.XPATH, tool_bar_dict[button]).click()
                time.sleep(0.2)