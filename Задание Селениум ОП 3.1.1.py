import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_pages import Login_page


class Tests():

    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\User.WSA34411\\PycharmProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("start Test")

        login_standart_user = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
        password_all = "secret_sauce"

        login = Login_page(driver)

        def text_products():
            text_products = driver.find_element(By.XPATH, "//span[@class = 'title']")
            value_text_products = text_products.text
            print(value_text_products)
            assert value_text_products == "Products"
            print("GOOD")

        def error_login():
            error_log = driver.find_element(By.XPATH, "//h3[@data-test='error']")
            value_error_log = error_log.text
            assert value_error_log == "Epic sadface: Sorry, this user has been locked out."
            print("Пользователь заблокирован")
            driver.refresh()

        for log in login_standart_user:
            try:
                login.authorization(log, password_all)
                button_menu = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
                text_products()
                logout = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()
            except: error_login()

        driver.close()



test = Tests()
test.test_select_product()









