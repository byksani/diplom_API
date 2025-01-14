import requests
import allure

from data import Urls


class OrderMethods:
    @allure.step("Создание заказа")
    def create_order(self, token, payload):
        response = requests.post(
            Urls.ORDERS,
            json=payload,
            headers={'Authorization': token}
        )

        if response.status_code == 500:
            return response.status_code, None

        else:
            return response.status_code, response.json()

    @allure.step("Получение списка заказов")
    def get_order_list(self, token):
        response = requests.get(
            Urls.ORDERS,
            headers={'Authorization': token}
        )

        return response.status_code, response.json()
