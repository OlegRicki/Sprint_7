import allure
import pytest
from base_api.api_order import CreateOrderApi


@allure.epic('Группа тестов на создание заказа')
class TestCreateOrder:
    @allure.title('Тест на создание заказа, проверяем код ответа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK AND GREY'], ['']])
    def test_create_order(self, color):
        order_api = CreateOrderApi()
        response = order_api.create_order_and_return_response(color=color)
        assert response.status_code == 201

    @allure.title('Тест на создание заказа, проверяем тело ответа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK AND GREY'], ['']])
    def test_create_order_body_response_body_contains_track(self, color):
        order_api = CreateOrderApi()
        response = order_api.create_order_and_return_response(color=color)

        assert 'track' in response.json()
