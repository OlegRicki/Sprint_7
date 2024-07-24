from base_api.test_base_api import BaseApi
from base_api.create_courier_api import CreateCourierApi


class TestCreateCourier(BaseApi):

    def test_create_courier(self):
        base_api = BaseApi()
        assert base_api.register_new_courier_and_return_login_password() is not None

    def test_fail_create_two_identical_couriers(self):
        courier_api = CreateCourierApi()
        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        login_pass = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        login_pass_two = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert login_pass != login_pass_two
        assert login_pass_two == []

    def test_fail_create_courier_without_one_argument(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = ''

        login_pass = courier_api.register_new_courier(login=login, password=password, first_name=firstName)
        assert login_pass == []

    def test_correct_response_code_after_creating_new_courier(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        text = courier_api.register_new_courier_return_text(login=login, password=password, first_name=firstName)
        assert text == '{"ok":true}'

    def test_fail_return_error_when_one_argument_absent_when_create(self):
        courier_api = CreateCourierApi()

        first_name = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        status_cod = courier_api.register_new_courier_absent_one_argument(password=password, first_name=first_name)
        assert status_cod == 400

    def test_create_courier_already_used_login(self):
        courier_api = CreateCourierApi()

        login = courier_api.generate_random_string(10)
        password = courier_api.generate_random_string(10)
        firstName = courier_api.generate_random_string(10)

        status_cod = courier_api.register_new_courier_return_status_cod(login=login, password=password,
                                                                        first_name=firstName)
        assert status_cod == 201
        password_two = courier_api.generate_random_string(10)
        firstName_two = courier_api.generate_random_string(10)

        status_code = courier_api.register_new_courier_return_status_cod(
            login=login, password=password_two, first_name=firstName_two)

        assert status_code == 409
