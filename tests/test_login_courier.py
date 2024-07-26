import allure

from base_api.login_api_courier import LoginApiCourier
from constans import Constants

constants = Constants()


@allure.epic('Группа тестов на авторизацию курьера')
class TestLoginCourier:
    @allure.title('Тест на авторизацию курьера, проверяем статус код и тело ответа')
    def test_login_courier(self):
        login = constants.LOGIN
        password = constants.PASSWORD

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Негативный тест на авторизацию курьера'
                  ' при пустом значении одного из аргументов, проверяем код и тело ответа')
    def test_fail_login_courier_use_one_argument(self):
        login = constants.LOGIN
        password = ''

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    @allure.title('Негативный тест на авторизацю курьера когда логин '
                  'или пароль не корректный, проверяем код и тело ответа')
    def test_fail_login_courier_when_login_or_password_incorrect(self):
        login = constants.LOGIN
        password = f'{constants.PASSWORD}test'

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title('Тест на авторизацю курьера, с данными не зарегистрированного курьера, проверяем код и тело ответа')
    def test_login_courier_when_login_and_password_use_non_existent_data(self):
        login = 'nesushestv'
        password = 'nesushestv'

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title('Тест на авторизацию курьера, проверяем что в ответе есть id курьера')
    def test_login_courier_return_id(self):
        login = constants.LOGIN
        password = constants.PASSWORD

        login_api = LoginApiCourier()
        response = login_api.login_courier_and_return_response(login, password)

        assert 'id' in response.json()
