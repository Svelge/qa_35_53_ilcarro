import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://icarro-v1.netlify.app/")

    yield driver

    driver.quit()