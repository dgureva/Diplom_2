import allure
import requests

from const import Const, MessageText

class TestLoginUser:


    @allure.title('Проверка авторизации пользователя')
    def test_authorization_user(self, helpers):
        data = helpers.create_new_user_and_get_authentication_data()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[0],
            "password": data[1],
        })
        assert response.status_code == 200
        assert MessageText.LOGIN_USER in response.text

    @allure.title('Проверка авторизации пользователя с некорректным email')
    def test_authorization_with_invalid_email(self, helpers):
        data = helpers.create_new_user_and_get_authentication_data()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[1],
            "password": data[2],
        })
        assert response.status_code == 401
        assert MessageText.INCORECT_LOGIN_DATA in response.text

    @allure.title('Проверка авторизации пользователя с некорректным паролем')
    def test_authorization_with_invalid_password(self, helpers):
        data = helpers.create_new_user_and_get_authentication_data()
        response = requests.post(Const.LOGIN_USER, data={
            "email": data[0],
            "password": data[2],
        })
        assert response.status_code == 401
        assert MessageText.INCORECT_LOGIN_DATA in response.text