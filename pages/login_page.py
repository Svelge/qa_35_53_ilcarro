from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    LOGIN_NAV_LINK = (By.XPATH, "//*[text()='Log in']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"[type='password']")
    LOGIN_BTN = (By.CSS_SELECTOR,"[type='submit']")
    SIGN_OUT_BTN = (By.XPATH,"//button[text()='Log out']")

    def __init__(self,driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()


    def fill_email(self,email):
        wait = WebDriverWait(self.driver, 5)
        email_input_element = wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))

        email_input_element.clear()
        email_input_element.send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()