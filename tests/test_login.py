from data.user_data import existing_user
from pages.login_page import LoginPage


INVALID_EMAIL = "invalid_email_format"
INVALID_PASSWORD = "ert23"

def test_login_success(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.confirmation_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True

def test_login_wrong_email(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.error_message_text() == "Wrong email format"
    assert login_page.submit_button_disabled()


def test_login_empty_email(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.error_message_text() == "Email is required"
    assert login_page.submit_button_disabled()

def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    wrong_password = "TotallyWrongPass123$"
    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(wrong_password)
    login_page.submit_login()

    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'

def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password("")
    login_page.submit_login()

    assert login_page.error_message_text() == "Password is required"
    assert login_page.submit_button_disabled()

