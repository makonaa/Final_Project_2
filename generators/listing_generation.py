import random
import string
import allure


class ListingGenerator:

    def __get_random_str(self):
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(15))
        return random_str

    def __get_random_listing_name(self):
        return self.__get_random_str()

    def __get_random_category(self):
        category_list = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
        return random.choice(category_list)

    def __get_random_condition(self):
        condition_list = ['Новый', 'Б/У']
        return random.choice(condition_list)

    def __get_random_city(self):
        city_list = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']
        return random.choice(city_list)

    def __get_random_description(self):
        return self.__get_random_str()

    def __get_random_price(self):
        return random.randint(100, 100000)

    @allure.step('Создаем данные для объявления')
    def get_listing_data(self):
        payload = {
            "name": self.__get_random_listing_name(),
            "category": self.__get_random_category(),
            "condition": self.__get_random_condition(),
            "city": self.__get_random_city(),
            "description": self.__get_random_description(),
            "price": self.__get_random_price()
        }
        return payload

    @allure.step('Меняем данные объявления под формат, ожидаемый бэкендом')
    def get_listing_multipart_data(self):
        listing_data = self.get_listing_data()
        return {key: (None, str(value)) for key, value in listing_data.items()}
