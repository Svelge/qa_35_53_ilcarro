import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AddCarPage(BasePage):
    CAR_WORK_URL = "https://icarro-v1.netlify.app/let-car-work"
    CAR_WORK_BTN = (By.CSS_SELECTOR, "[href='/let-car-work']")
    CITY_INPUT = (By.ID, "city")
    MANUFACTURE_INPUT = (By.CSS_SELECTOR, "[name='manufacture']")
    MODEL_INPUT = (By.CSS_SELECTOR, "[name='model']")
    YEAR_INPUT = (By.CSS_SELECTOR, "[name='year']")
    FUEL_SELECT = (By.CSS_SELECTOR, "[name='fuel']")
    GEAR_SELECT = (By.CSS_SELECTOR, "[name='gear']")
    WD_SELECT = (By.CSS_SELECTOR, "[name='wheelsDrive']")
    SEATS_INPUT = (By.CSS_SELECTOR, "[name='seats']")
    CAR_CLASS_INPUT = (By.CSS_SELECTOR, "[name='carClass']")
    SERIAL_NUMBER_INPUT = (By.CSS_SELECTOR, "[name='serialNumber']")
    PRICE_INPUT = (By.CSS_SELECTOR, "[name='pricePerDay']")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error']")

    def open_car_form(self):
        self.click(self.CAR_WORK_BTN)
        time.sleep(2)

    def fill_city(self,city):
        self.fill(self.CITY_INPUT, city)

        option_locator = (By.CSS_SELECTOR, f"[data-testid='city-option'][data-value='{city}]")
        option = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(option_locator))
        option.click()

    def fill_manufacture(self, manufacture):
        self.fill(self.MANUFACTURE_INPUT, manufacture)

    def fill_model(self, model):
        self.fill(self.MODEL_INPUT, model)

    def fill_year(self, year):
        self.fill(self.YEAR_INPUT, year)

