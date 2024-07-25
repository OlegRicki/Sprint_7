import allure
import requests
import random
import string
from constans import Constants
from base_api.test_base_api import BaseApi

constans = Constants()

class CreateCourierApi(BaseApi):
    @allure.title('Зарегистрировать нового курьера')
    def register_new_courier(self, login: str, password: str, first_name: str):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        return response

    @allure.title('сгенерировать строку')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.title('Зарегистрировать нового курьера и вернуть статус код')
    def register_new_courier_return_status_cod(self, login: str, password: str, first_name: str):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        return response.status_code

    @allure.title('Зарегистрировать нового курьера и вернуть текст')
    def register_new_courier_return_text(self, login: str, password: str, first_name: str):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        return response.text

    @allure.title('Зарегистрировать нового курьера без обязательного поля ')
    def register_new_courier_absent_one_argument(self, password: str, first_name: str):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # собираем тело запроса
        payload = {
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        return response
