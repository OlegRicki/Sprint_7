from base_api.api_order import CreateOrderApi
from base_api.test_base_api import BaseApi


class TestListOrder(BaseApi):
    def test_get_order_list(self):
        order_api = CreateOrderApi()
        r = order_api.get_list_order()
        assert 'orders' in r
