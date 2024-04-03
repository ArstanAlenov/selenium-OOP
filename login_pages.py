from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):


        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")))
        user_name.send_keys(login_name)
        print(f"Input Login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(login_password)
        print(f"Input Password")

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@type = 'submit']"))).click()
        print(f"Click Login Button")
