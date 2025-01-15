import allure

from data import Ingredients


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_success(self, create_order_for_user):
        status_code, response_context = create_order_for_user

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['success'] == True, \
            f"Ожидался success=True, а получили: {response_context}"

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_without_auth_success(self, order_methods):
        payload = {
            'ingredients': Ingredients.DEFAULT_INGREDIENTS
        }

        status_code, response_context = order_methods.create_order('', payload)

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['success'] == True, \
            f"Ожидался success=True, а получили: {response_context}"

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_error(self, order_methods):
        payload = {
            'ingredients': []
        }

        status_code, response_context = order_methods.create_order('', payload)

        assert status_code == 400, \
            f"Ожидался статус 400, а получили статус {status_code}."

        assert response_context['success'] == False, \
            f"Ожидался success=False, а получили: {response_context}"

    @allure.title("Создание заказа с неверными ингредиентами")
    def test_create_order_with_wrong_ingredients_error(self, order_methods):
        payload = {
            'ingredients': Ingredients.INVALID_INGREDIENTS
        }

        status_code, response_context = order_methods.create_order('', payload)
        assert status_code == 500, \
            f"Ожидался статус 500, а получили статус {status_code}"
