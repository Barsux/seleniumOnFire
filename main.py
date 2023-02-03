from selenium import webdriver
from selenium.webdriver.common.by import By
import time

txt = "Декоративно-прикладное творчество"
num = "2300000123012"

options = None
driver = None


def init():
    global options, driver
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    driver = webdriver.Chrome(
        executable_path="/home/cain/PycharmProject/selenium_python/chromedriver/chromedriver",
        options=options
    )


def wait():
    print("Жду 2 сек")
    time.sleep(2)


def intro():
    print("MADE BY IGOR COUNCIL")


def run():
    global options, driver
    # Заход на страницу
    driver.get("https://ogon.moscow/galereya/odv/2023")
    print("Зашёл")

    wait()
    # Ищем категорию по названию и херачим по ней
    driver.find_element(By.XPATH, f"//h2[contains(text(), '{txt}')]").click()
    print("Раскрыл категорию")
    wait()
    # Ищем ту часть где нужная нам заявка
    child = driver.find_element(By.XPATH, f"//div[contains(text(), '{num}')]")
    print("Нашёл нужный пункт")
    wait()
    # Ищем родителя т.к. лайк находиться с названием под одним родителем
    parent = child.find_element(By.XPATH, "..")
    print("Нашёл родителя")
    wait()
    # Ищем лайк и херачим по нему
    parent.find_element(By.XPATH, ".//i").click()
    print("Лайкнул")
    time.sleep(10)


def main():
    intro()
    init()
    run()


if __name__ == "__main__":
    main()
