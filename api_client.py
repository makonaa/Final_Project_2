from generators.listing_generation import ListingGenerator
from generators.user_generation import DataGenerator
from endpoint_executions import sign_up_user, create_listing
from custom_exceptions import FailedToSignupNewUser, FailedToCreateNewListing
import allure


class ApiClient:
    def __init__(self):
        self.data_generator = DataGenerator()
        self.listing_generator = ListingGenerator()

    @allure.step('Регистрируем юзера и возвращаем его полные данные')
    def sign_up_and_return_user_data(self):
        user_data = self.data_generator.get_user_for_signup()
        response = sign_up_user(user_data)
        if response.status_code != 201:
            raise FailedToSignupNewUser(
                "Failed to sign up new user"
                f'Error code: {response.status_code}, payload: {response.text}'
            )
        return user_data

    @allure.step('Регистрируем юзера и возвращаем его данные для логина')
    def get_user_data_for_sign_in(self):
        user_data = self.sign_up_and_return_user_data()
        del user_data["submitPassword"]
        return user_data

    @allure.step('Регистрируем юзера и возвращаем его токен аутентификации')
    def get_auth_headers(self):
        user = self.data_generator.get_user_for_signup()
        response = sign_up_user(user)
        auth_token = response.json()['access_token']['access_token']
        payload = {
            "Authorization": f"Bearer {auth_token}"
        }
        return payload

    @allure.step('Создаем объявление и возвращаем его id и Bearer токен автора объявления')
    def get_listing_id_and_auth_headers(self) -> tuple[str, dict]:
        headers = self.get_auth_headers()
        listing_data = self.listing_generator.get_listing_multipart_data()
        response = create_listing(files=listing_data, headers=headers)
        if response.status_code != 201:
            raise FailedToCreateNewListing()
        listing_id = response.json()['id']
        return listing_id, headers
