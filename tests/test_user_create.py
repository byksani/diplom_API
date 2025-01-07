import pytest
import allure


class TestCreateUser:
    @allure.story("Создание нового пользователя с заполненными полями")
    def test_new_user_with_all_fields_success(self, created_user):
        status_code, response_context = created_user
        assert status_code == 200 and response_context['success'] == True, \
            f"Ожидался статус 200 и success=False, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Попытка создания уже зарегистрированного пользователя")
    def test_create_already_created_user_error(self, auth_methods, created_user, unique_user_data):
        status_code, response_context = auth_methods.create_user(unique_user_data)
        assert status_code == 403 and response_context['message'] == 'User already exists', \
            f"Ожидался статус 403 и success=False, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Попытка создания пользователя без одного из обязательных полей")
    @pytest.mark.parametrize('payload', [
        {'email': 'test@yandex.ru', 'password': '12345678'},
        {'password': '12345678', 'name': 'test_name'},
        {'email': 'test@yandex.ru', 'name': 'test_name'},
    ])
    def test_create_user_without_required_field_error(self, auth_methods, payload):
        status_code, response_context = auth_methods.create_user(payload)
        assert status_code == 403 and response_context['message'] == 'Email, password and name are required fields', \
            f"Ожидался статус 403 и success=False, а получили статус {status_code} и ответ: {response_context}"
