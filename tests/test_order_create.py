import allure


class TestCreateOrder:
    @allure.story("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_success(self, create_order_for_user):
        status_code, response_context = create_order_for_user
        assert status_code == 200 and response_context['success'] == True, \
            f"Ожидался статус 200 и success=True, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_without_auth_success(self, order_methods):
        payload = {
            'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']
        }

        status_code, response_context = order_methods.create_order('', payload)
        assert status_code == 200 and response_context['success'] == True, \
            f"Ожидался статус 200 и success=True, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_error(self, order_methods):
        payload = {
            'ingredients': []
        }

        status_code, response_context = order_methods.create_order('', payload)
        assert status_code == 400 and response_context['success'] == False, \
            f"Ожидался статус 400 и success=False, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Создание заказа с неверными ингредиентами")
    def test_create_order_with_wrong_ingredients_error(self, order_methods):
        payload = {
            'ingredients': ['61c0c5a71d1f82001bdooo6d', '61c0c5a71d1f82001bdnnn6f']
        }

        status_code = order_methods.create_order('', payload)
        assert status_code == 500, \
            f"Ожидался статус 500, а получили статус {status_code}"
