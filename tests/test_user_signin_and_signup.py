from endpoint_executions import sign_up_user, sign_in_user
import allure


class TestUserSignInAndSignup:
    @allure.title('Тест - регистрируемся новым юзером')
    def test_user_sign_up_successful(self, data_generator):
        user_data = data_generator.get_user_for_signup()
        response = sign_up_user(user_data)
        assert response.status_code == 201

    @allure.title('Тест - регистрируемся уже существующим юзером')
    def test_repeated_sign_up_for_registered_user(self, api_client):
        user_data = api_client.sign_up_and_return_user_data()
        response = sign_up_user(user_data)
        assert response.status_code == 400

    @allure.title('Тест - логинимся зарегистированным юзером')
    def test_sign_in_for_registered_user_successful(self, api_client):
        user_data = api_client.get_user_data_for_sign_in()
        response = sign_in_user(user_data)
        assert response.status_code == 201
