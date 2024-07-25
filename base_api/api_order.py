import allure
import requests

from constans import Constants
from base_api.test_base_api import BaseApi

constants = Constants()


class CreateOrderApi(BaseApi):
    URL_TEST = constants.ORDER_API

    @allure.title('Создать заказ и вернуть статус код')
    def create_order_and_return_response(self, color: str):
        data = {
            "firstName": 'Naruto',
            "lastName": 'Uchiha',
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": '+7 800 355 35 35',
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = requests.post(url=self.URL_TEST, json=data)
        return response
    @allure.title('Создать заказ и вернуть тело запроса')
    def create_order_and_return_body(self, color: str):
        data = {
            "firstName": 'Naruto',
            "lastName": 'Uchiha',
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": '+7 800 355 35 35',
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = requests.post(url=self.URL_TEST, json=data)
        return response.json()

    @allure.title('Получить список заказов')
    def get_list_order(self):
        response = requests.get(url=self.URL_TEST)
        return response
