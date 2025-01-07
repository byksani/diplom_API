import pytest
import random
import string
import requests

from methods.auth_methods import AuthMethods
from methods.orders_methods import OrderMethods


@pytest.fixture()
def auth_methods():
    return AuthMethods()

@pytest.fixture()
def order_methods():
    return OrderMethods()

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@pytest.fixture()
def unique_user_data():

    name = generate_random_string(6)
    password = generate_random_string(10)

    payload = {
        'email': f'{name}@yandex.ru',
        'password': password,
        'name': name
    }

    return payload

@pytest.fixture()
def created_user(auth_methods, unique_user_data):
    status_code, response_context = auth_methods.create_user(unique_user_data)

    yield status_code, response_context

    auth_methods.delete_user(response_context['accessToken'])

@pytest.fixture()
def logged_in_user(auth_methods, unique_user_data):
    auth_methods.create_user(unique_user_data)
    status_code, response_context = auth_methods.login_user(unique_user_data)

    yield status_code, response_context

    auth_methods.delete_user(response_context['accessToken'])

@pytest.fixture()
def create_order_for_user(order_methods, created_user):
    _, response_context = created_user
    token = response_context['accessToken']

    payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    status_code, response_context = order_methods.create_order(token, payload)

    yield status_code, response_context
