import pytest
import allure

from data import SystemMessages


class TestLoginUser:
    @allure.title("Логин уже зарегистрированного пользователя")
    def test_login_already_created_user_success(self, logged_in_user):
        status_code, response_context = logged_in_user

        assert status_code == 200, \
            f"Ожидался статус 200, а получили статус {status_code}."

        assert response_context['success'] == True, \
            f"Ожидался success=True, а получили ответ: {response_context}"

    @allure.title("Логин с неверными данными")
    @pytest.mark.parametrize('email, password', [
        ('nonexistent_user@example.com', 'wrongpassword123'),
        ('', 'password123'),
        ('test@example.com', '')
    ])
    def test_login_with_invalid_credentials_error(self, auth_methods, email, password):
        payload = {'email': email, 'password': password}
        status_code, response_context = auth_methods.login_user(payload)

        assert status_code == 401, \
            f"Ожидался статус 401, а получили статус {status_code}."

        assert response_context['message'] == SystemMessages.INVALID_EMAIL_OR_PASSWORD, \
            f"Ожидалось сообщение {SystemMessages.INVALID_EMAIL_OR_PASSWORD}, а получили ответ: {response_context}"
