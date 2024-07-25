import allure
import requests

from constans import Constants
from base_api.test_base_api import BaseApi

constants = Constants()


class LoginApiCourier(BaseApi):
    URL_TEST = constants.COURIER_LOGIN_API

    @allure.title('Авторизовать курьера и вернуть статус код')
    def login_courier_and_return_status_code(self, login: str, password: str):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url=self.URL_TEST, data=data)
        return response.status_code

    @allure.title('Авторизовать курьера и вернуть id ')
    def login_courier_and_return_id(self, login: str, password: str):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url=self.URL_TEST, data=data)
        return response.json()
