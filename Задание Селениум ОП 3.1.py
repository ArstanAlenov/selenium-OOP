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

        login.authorization(login_standart_user[0], password_all)
        button_menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
        text_products()
        logout = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()

        login.authorization(login_standart_user[1], password_all)
        driver.refresh()

        login.authorization(login_standart_user[2], password_all)
        button_menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
        text_products()
        logout = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()


        login.authorization(login_standart_user[3], password_all)
        button_menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
        text_products()
        logout = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()

        driver.close()
        driver.quit()









test = Tests()
test.test_select_product()
