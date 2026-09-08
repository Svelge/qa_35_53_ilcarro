import random
import uuid

from data.user_data import create_user
from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()


    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registered"
    assert registration_page.confirmation_message() == "You are logged in success"
    registration_page.close_window()


def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(name = "")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()


def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)

    user = create_user(last_name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Last name is required"
    assert registration_page.submit_button_disabled()

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(email="tony_mollygmail.com")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Wrong email format"
    assert registration_page.submit_button_disabled()

def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(email="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Email is required"
    assert registration_page.submit_button_disabled()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(password="P123$")


    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)

    user = create_user(password="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password is required"
    assert registration_page.submit_button_disabled()

def test_registration_without_check_box(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()


    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "You must accept the terms"
    assert registration_page.submit_button_disabled()

