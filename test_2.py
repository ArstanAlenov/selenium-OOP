
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_pages import Login_page


class Test_2():

    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\User.WSA34411\\PycharmProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("start Test")

        login_problem_user = "problem_user"
        password_all = "secret_sauce"

        login = Login_page(driver)
        login.authorization(login_problem_user, password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@id,'labs-backpack')]")))
        select_product.click()
        print("click select product")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
        print("click enter_shopping_cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("test succefull")




test = Test_2()
test.test_select_product()