import pytest
import allure

from data import SystemMessages


class TestCreateUser:
    @allure.step("Создание нового пользователя с заполненными полями")
    def test_new_user_with_all_fields_success(self, created_user):
        status_code, response_context = created_user

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['success'] == True, \
            f"Ожидался success=False, а получили ответ: {response_context}"

    @allure.step("Попытка создания уже зарегистрированного пользователя")
    def test_create_already_created_user_error(self, auth_methods, created_user, unique_user_data):
        status_code, response_context = auth_methods.create_user(unique_user_data)

        assert status_code == 403, \
            f"Ожидался статус 403, а получили статус {status_code}."

        assert response_context['message'] == SystemMessages.USER_ALREADY_EXISTS, \
            f"Ожидался ошибка {SystemMessages.USER_ALREADY_EXISTS}, а получили ответ: {response_context}"

    @allure.step("Попытка создания пользователя без одного из обязательных полей")
    @pytest.mark.parametrize('payload', [
        {'email': 'test@yandex.ru', 'password': '12345678'},
        {'password': '12345678', 'name': 'test_name'},
        {'email': 'test@yandex.ru', 'name': 'test_name'},
    ])
    def test_create_user_without_required_field_error(self, auth_methods, payload):
        status_code, response_context = auth_methods.create_user(payload)

        assert status_code == 403, \
            f"Ожидался статус 403, а получили статус {status_code}."

        assert response_context['message'] == SystemMessages.REQUIRED_FIELDS_MISSING, \
            f"Ожидался ответ {SystemMessages.REQUIRED_FIELDS_MISSING}, а получили ответ: {response_context}"
