import pytest
from base_api.test_base_api import BaseApi
from base_api.api_order import CreateOrderApi


class TestCreateOrder(BaseApi):

    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK AND GREY'], ['']])
    def test_create_order(self, color):
        order_api = CreateOrderApi()
        status_code = order_api.create_order_and_return_status_code(color=color)
        assert status_code == 201

    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK AND GREY'], ['']])
    def test_create_order_body_response_body_contains_track(self, color):
        order_api = CreateOrderApi()
        body = order_api.create_order_and_return_body(color=color)
        assert 'track' in body
