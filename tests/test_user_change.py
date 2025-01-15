import pytest
import allure


class TestChangeUser:
    @allure.title("Изменение имени и email авторизованного пользователя")
    @pytest.mark.parametrize('field, new_value', [
        ('email', 'updated_email@yandex.ru'),
        ('name', 'UpdatedName')
    ])
    def test_change_user_name_and_email_success(self, auth_methods, created_user, field, new_value):
        _, response_context = created_user
        token = response_context['accessToken']

        payload = {field: new_value}

        status_code, response_context = auth_methods.change_user(token, payload)

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['user'][field] == new_value, \
            f"Ожидалось что {field} теперь содержит {new_value}, а получили ответ: {response_context}"

    @allure.title("Изменение пароля авторизованного пользователя")
    def test_change_user_password_success(self, auth_methods, created_user):
        _, response_context = created_user
        token = response_context['accessToken']

        payload = {'password': 'new_password123'}

        status_code, response_context = auth_methods.change_user(token, payload)

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['success'] == True, \
            f"Ожидался success=True, а получили: {response_context}"

    @allure.title("Попытка изменения данных пользователя без авторизации")
    @pytest.mark.parametrize('field, new_value', [
        ('email', 'updated_email@yandex.ru'),
        ('password', 'new_password123'),
        ('name', 'UpdatedName')
    ])
    def test_change_user_data_without_auth_error(self, auth_methods, created_user, field, new_value):
        payload = {field: new_value}

        status_code, response_context = auth_methods.change_user('', payload)

        assert status_code == 401, \
            f"Ожидался статус 401, а получили статус {status_code}."

        assert response_context['success'] == False, \
            f"Ожидался success=False, а получили: {response_context}"
