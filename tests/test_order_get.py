import allure

from data import SystemMessages


class TestGetOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_for_user_success(self, create_order_for_user, created_user, order_methods):
        _, response_context = created_user
        token = response_context['accessToken']

        status_code, response_context = order_methods.get_order_list(token)

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert len(response_context['orders']) == 1, \
            f"Ожидался только один заказ, а получено {len(response_context['orders'])}"

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_for_user_without_auth_error(self, create_order_for_user, order_methods):
        status_code, response_context = order_methods.get_order_list('')

        assert status_code == 401, \
            f"Ожидался статус 401, а получили статус {status_code}."

        assert response_context['message'] == SystemMessages.UNAUTHORIZED, \
            f"Ожидалось сообщение {SystemMessages.UNAUTHORIZED}, а получили ответ: {response_context}"
