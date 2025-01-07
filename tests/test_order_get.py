import allure


class TestGetOrders:
    @allure.story("Получение заказов авторизованного пользователя")
    def test_get_orders_for_user_success(self, create_order_for_user, created_user, order_methods):
        _, response_context = created_user
        token = response_context['accessToken']

        status_code, response_context = order_methods.get_order_list(token)

        assert status_code == 200 and len(response_context['orders']) == 1, \
            f"Ожидался статус 200 и только один заказ, а получен статус {status_code} и {len(response_context['orders'])} заказов"

    @allure.story("Получение заказов неавторизованного пользователя")
    def test_get_orders_for_user_without_auth_error(self, create_order_for_user, order_methods):
        status_code, response_context = order_methods.get_order_list('')

        assert status_code == 401 and response_context['message'] == 'You should be authorised', \
            f"Ожидался статус 401 и сообщение 'You should be authorised', а получили статус {status_code} и ответ: {response_context}"