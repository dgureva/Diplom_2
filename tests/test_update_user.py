import allure
import requests

from const import Const, MessageText

class TestUpdateUser:

    @allure.title('Проверка изменения email авторизованного пользователя')
    def test_update_email_user_with_authorization(self, helpers, get_token):
        token = get_token
        email, name, password = helpers.generate_data()
        payload = {
            "email": email
            }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(Const.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.UPDATE_USER in response.text

    @allure.title('Проверка изменения пароля авторизованного пользователя')
    def test_update_password_user_with_authorization(self, helpers, get_token):
        token = get_token
        email, name, password = helpers.generate_data()
        payload = {
            "password": password
            }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(Const.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.UPDATE_USER in response.text

    @allure.title('Проверка изменения имени авторизованного пользователя')
    def test_update_name_user_with_authorization(self, helpers, get_token):
        token = get_token
        email, name, password = helpers.generate_data()
        payload = {
            "name": name
            }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(Const.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.UPDATE_USER in response.text

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    def test_update_data_user_without_authorization(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            "email": email,
            "password": password
            }
        headers = {"Content-type": "application/json"}
        response = requests.patch(Const.UPDATE_DATA, headers=headers, json=payload)
        assert response.status_code == 401
        assert MessageText.UPDATE_USER_UNSUCCESSFULLY in response.text