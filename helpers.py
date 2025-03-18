import random
import string

import allure
import requests

from const import Const


class Helpers:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self, domain="ya.ru", username_prefix="dgureva_13"):
        random_number = random.randint(0, 9999)
        login = f"{username_prefix}{random_number}"
        email = f"{login}@{domain}"
        return email

    def generate_data(self):
        email = self.generate_random_email()
        name = self.generate_random_string(10)
        password = self.generate_random_string(10)
        return email, name, password

    @allure.step("Создание нового пользователя и получение данных для авторизации")
    def create_new_user_and_get_authentication_data(self):
        login_pass = []

        email = self.generate_random_email()
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": name,
        }

        response = requests.post(Const.CREATE_USER, data=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)

        return login_pass