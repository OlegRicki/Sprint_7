import allure
import random
import string

from constans import Constants

constants = Constants()


class BaseApi:

    @allure.title('сгенерировать строку')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
