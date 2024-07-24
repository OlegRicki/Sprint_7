import requests
import random
import string

from base_api.test_base_api import BaseApi


class CreateCourierApi(BaseApi):

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

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

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
        return response.status_code
