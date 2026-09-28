from Urls import *
import requests
import allure

@allure.step('Регистрируем юзера')
def sign_up_user(payload:dict) -> requests.Response:
    return requests.post(SIGN_UP_URL, data=payload)

@allure.step('Логин юзера')
def sign_in_user(payload:dict) -> requests.Response:
    return requests.post(SIGN_IN_URL, data=payload)

@allure.step('Создаем объявление')
def create_listing(files:dict[str, tuple[None, str]], headers:dict) -> requests.Response:
    return requests.post(CREATE_LISTING_URL, files=files, headers=headers)

@allure.step('Обновляем объявление')
def update_listing(files:dict[str, tuple[None, str]], headers:dict, listing_id:int) -> requests.Response:
    return requests.patch(UPDATE_LISTING_URL.substitute(listing_id=listing_id), files=files, headers=headers)

@allure.step('Удаляем объявление')
def delete_listing(headers:dict, listing_id:int) -> requests.Response:
    return requests.delete(DELETE_LISTING_URL.substitute(listing_id=listing_id), headers=headers)
