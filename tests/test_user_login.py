import pytest
import allure


class TestLoginUser:
    @allure.story("Логин уже зарегистрированного пользователя")
    def test_login_already_created_user_success(self, logged_in_user):
        status_code, response_context = logged_in_user
        assert status_code == 200 and response_context['success'] == True, \
            f"Ожидался статус 200 и success=True, а получили статус {status_code} и ответ: {response_context}"

    @allure.story("Логин с неверными данными")
    @pytest.mark.parametrize('email, password', [
        ('nonexistent_user@example.com', 'wrongpassword123'),
        ('', 'password123'),
        ('test@example.com', '')
    ])
    def test_login_with_invalid_credentials_error(self, auth_methods, email, password):
        payload = {'email': email, 'password': password}
        status_code, response_context = auth_methods.login_user(payload)

        assert status_code == 401 and response_context['message'] == 'email or password are incorrect', \
            f"Ожидался статус 401 и сообщение 'email or password are incorrect', а получили статус {status_code} и ответ: {response_context}"
