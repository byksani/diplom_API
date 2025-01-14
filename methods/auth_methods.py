import requests
import allure

from data import Urls


class AuthMethods:
    @allure.step("Создание пользователя")
    def create_user(self, payload):
        response = requests.post(Urls.REGISTER, json=payload)
        return response.status_code, response.json()

    @allure.step("Логин пользователя")
    def login_user(self, payload):
        response = requests.post(Urls.LOGIN, json=payload)
        return response.status_code, response.json()

    @allure.step("Изменение данных пользователя")
    def change_user(self, token, payload):
        response = requests.patch(
            Urls.USER,
            headers={'Authorization': token},
            json=payload
        )
        return response.status_code, response.json()

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        response = requests.delete(
            Urls.USER,
            headers={'Authorization': token}
        )
        return response.status_code, response.json()
