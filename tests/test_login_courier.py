from base_api.test_base_api import BaseApi
from base_api.login_api_courier import LoginApiCourier
from constans import Constants

constants = Constants()


class TestLoginCourier:

    def test_login_courier(self):
        login = constants.LOGIN
        password = constants.PASSWORD

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 200

    def test_fail_login_courier_use_one_argument(self):
        login = constants.LOGIN
        password = ''

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    def test_fail_login_courier_when_login_or_password_incorrect(self):
        login = constants.LOGIN
        password = f'{constants.PASSWORD}test'

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    def test_login_courier_when_login_and_password_use_non_existent_data(self):
        login = 'nesushestv'
        password = 'nesushestv'

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    def test_login_courier_return_id(self):
        login = constants.LOGIN
        password = constants.PASSWORD

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)

        assert 'id' in response.json()
