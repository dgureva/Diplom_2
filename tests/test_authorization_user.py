import allure
import requests

from const import Const, MessageText
from helpers import Helpers


class TestLoginUser:

    @allure.title('Проверка авторизации пользователя')
    def test_authorization_user(self):
        helpers = Helpers()
        data = helpers.create_new_user_and_get_authentication_data()

        with allure.step("Отправка POST-запроса"):
            response = requests.post(Const.LOGIN_USER, data={
                "email": data[0],
                "password": data[1],
            })

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 200
            assert MessageText.LOGIN_USER in response.text

    @allure.title('Проверка авторизации пользователя с некорректным email')
    def test_authorization_with_invalid_email(self):
        helpers = Helpers()
        data = helpers.create_new_user_and_get_authentication_data()

        with allure.step("Отправка POST-запроса с некорректным email"):
            response = requests.post(Const.LOGIN_USER, data={
                "email": data[1],  # Неверный email
                "password": data[2],
            })

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 401
            assert MessageText.INCORECT_LOGIN_DATA in response.text

    @allure.title('Проверка авторизации пользователя с некорректным паролем')
    def test_authorization_with_invalid_password(self):
        helpers = Helpers()
        data = helpers.create_new_user_and_get_authentication_data()

        with allure.step("Отправка POST-запроса с некорректным паролем"):
            response = requests.post(Const.LOGIN_USER, data={
                "email": data[0],
                "password": data[2],  # Неверный пароль
            })

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 401
            assert MessageText.INCORECT_LOGIN_DATA in response.text