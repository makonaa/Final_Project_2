from faker import Faker
import random
import string
import allure


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def __get_random_str(self):
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(15))
        return random_str

    def __get_random_email(self) -> str:
        return f'{self.__get_random_str()}@{self.fake.free_email_domain()}'

    def __get_random_password(self) -> str:
        return self.fake.password()

    @allure.step('Создаем данные пользователя')
    def get_user_for_signup(self) -> dict:
        gen_password = self.__get_random_password()
        user_dict = {
            "email": self.__get_random_email(),
            "password": gen_password,
            "submitPassword": gen_password
        }
        return user_dict
