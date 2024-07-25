from base_api.api_order import CreateOrderApi
from base_api.test_base_api import BaseApi


class TestListOrder:
    def test_get_order_list(self):
        order_api = CreateOrderApi()
        response = order_api.get_list_order()
        assert response.status_code == 200
        assert 'orders' in response.json()
