import allure

from base_api.api_order import CreateOrderApi


@allure.epic('Группа тестов на получение списка заказов')
class TestListOrder:
    @allure.title('Тест на получение списка заказов, проверяем код ответа и тело ответа')
    def test_get_order_list(self):
        order_api = CreateOrderApi()
        response = order_api.get_list_order()
        assert response.status_code == 200
        assert 'orders' in response.json()
