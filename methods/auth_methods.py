import requests
import allure

from data import REGISTER, LOGIN, USER


class AuthMethods:
    @allure.story("Создание пользователя")
    def create_user(self, payload):
        response = requests.post(REGISTER, json=payload)
        return response.status_code, response.json()

    @allure.story("Логин пользователя")
    def login_user(self, payload):
        response = requests.post(LOGIN, json=payload)
        return response.status_code, response.json()

    @allure.story("Изменение данных пользователя")
    def change_user(self, token, payload):
        response = requests.patch(
            USER,
            headers={'Authorization': token},
            json=payload
        )
        return response.status_code, response.json()

    @allure.story("Удаление пользователя")
    def delete_user(self, token):
        response = requests.delete(
            USER,
            headers={'Authorization': token}
        )
        return response.status_code, response.json()
