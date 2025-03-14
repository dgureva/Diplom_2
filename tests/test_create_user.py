import allure
import requests

from const import Const, MessageText


class TestCreareUser:

    @allure.title('Проверка успешного создания нового пользователя')
    def test_create_new_user_successfully(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "password": password,
            "name": name,
            }
        response = requests.post(Const.CREATE_USER, data=payload)
        assert response.status_code == 200
        assert MessageText.CREATE_USER in response.text

    @allure.title('Проверка невозможности создания одинаковых пользователей')
    def test_create_user_twice(self, helpers):
        data = helpers.create_new_user_and_get_authentication_data()
        response = requests.post(Const.CREATE_USER, data={
            "email": data[0],
            "password": data[1],
            "name": data[2]
        })
        assert response.status_code == 403
        assert MessageText.CREATE_USER_TWICE in response.text

    @allure.title('Проверка невозможности создания пользователя без ввода имени')
    def test_create_user_without_name(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "password": password,
            }
        response = requests.post(Const.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка невозможности создания пользователя без ввода email')
    def test_create_user_without_email(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            "password": password,
            "name": name,
            }
        response = requests.post(Const.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка невозможности создания  пользователя без ввода пароля')
    def test_create_user_without_password(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "name": name,
            }
        response = requests.post(Const.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert MessageText.CREATE_COURIER_WITHOUT_PASSWORD in response.text