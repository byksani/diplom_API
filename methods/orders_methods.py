import requests
import allure

from data import ORDERS


class OrderMethods:
    @allure.story("Создание заказа")
    def create_order(self, token, payload):
        response = requests.post(
            ORDERS,
            json=payload,
            headers={'Authorization': token}
        )

        if response.status_code == 500:
            return response.status_code

        else:
            return response.status_code, response.json()

    @allure.story("Получение списка заказов")
    def get_order_list(self, token):
        response = requests.get(
            ORDERS,
            headers={'Authorization': token}
        )

        return response.status_code, response.json()
