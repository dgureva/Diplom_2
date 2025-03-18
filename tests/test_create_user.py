import allure
import requests

from const import Const, MessageText
from helpers import Helpers

class TestCreateUser:

    @allure.title('Проверка успешного создания нового пользователя')
    def test_create_new_user_successfully(self):
        helpers = Helpers()
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "password": password,
            "name": name,
        }

        with allure.step("Отправка POST-запроса для создания нового пользователя"):
            response = requests.post(Const.CREATE_USER, data=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 200
            assert MessageText.CREATE_USER in response.text

    @allure.title('Проверка невозможности создания одинаковых пользователей')
    def test_create_user_twice(self):
        helpers = Helpers()
        data = helpers.create_new_user_and_get_authentication_data()
        payload = {
            "email": data[0],
            "password": data[1],
            "name": data[2]
        }

        with allure.step("Отправка POST-запроса на создание уже существующего пользователя"):
            response = requests.post(Const.CREATE_USER, data=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 403
            assert MessageText.CREATE_USER_TWICE in response.text

    @allure.title('Проверка невозможности создания пользователя без ввода имени')
    def test_create_user_without_name(self):
        helpers = Helpers()
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "password": password,
        }

        with allure.step("Отправка POST-запроса без указания имени пользователя"):
            response = requests.post(Const.CREATE_USER, data=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 403
            assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка невозможности создания пользователя без ввода email')
    def test_create_user_without_email(self):
        helpers = Helpers()
        email, name, password = helpers.generate_data()
        payload = {
            "password": password,
            "name": name,
        }

        with allure.step("Отправка POST-запроса без указания email пользователя"):
            response = requests.post(Const.CREATE_USER, data=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 403
            assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка невозможности создания пользователя без ввода пароля')
    def test_create_user_without_password(self):
        helpers = Helpers()
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "name": name,
        }

        with allure.step("Отправка POST-запроса без указания пароля пользователя"):
            response = requests.post(Const.CREATE_USER, data=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 403
            assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text