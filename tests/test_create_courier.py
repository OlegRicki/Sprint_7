import allure

from base_api.create_courier_api import CreateCourierApi


@allure.epic('Группа тестов на создание курьера')
class TestCreateCourier:
    @allure.title('Тест на создание курьера, проверяем код ответа и тело ответа')
    def test_create_courier(self):
        courier_api = CreateCourierApi()
        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)
        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Негативный тест на создание двух одинаковых курьеров, проверяем код ответа и тело ответа')
    def test_fail_create_two_identical_couriers(self):
        courier_api = CreateCourierApi()
        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title(
        'Негативный тест на создание курьера без одного обязательного аргумента, проверяем код ответа и тело ответа')
    def test_fail_create_courier_without_one_argument(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = ''
        firstName = courier_api.generate_random_string(10)

        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Тест на создание курьера, проверяем корректный код ответа и тело ответа ')
    def test_correct_response_code_after_creating_new_courier(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title(
        'Негативный тест на создание курьера, если один аргумент пропущен, проверяем код ответа и тело ответа')
    def test_fail_return_error_when_one_argument_absent_when_create(self):
        courier_api = CreateCourierApi()

        first_name = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        response = courier_api.register_new_courier_absent_one_argument(password=password, first_name=first_name)
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Тест на создание курьера с уже импользованным логином, проверяем код ответа и тело ответа')
    def test_create_courier_already_used_login(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        response = courier_api.register_new_courier(login=login, password=password, first_name=firstName)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

        password_two = courier_api.generate_random_string(10)
        firstName_two = courier_api.generate_random_string(10)

        response = courier_api.register_new_courier(login=login, password=password_two, first_name=firstName_two)

        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
