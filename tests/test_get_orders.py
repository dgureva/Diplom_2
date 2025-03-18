import allure
import requests

from const import Ingredients, MessageText, Const

class TestGetOrders:

    @allure.title('Проверка получения заказа конкретного пользователя c авторизацией')
    def test_get_order_successfully(self, get_token):
        token = get_token
        payload = {
            "ingredients": [Ingredients.BUN, Ingredients.MEAT_PROTOSTOMIA, Ingredients.SPICY_SAUSE]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}

        with allure.step("GET-запрос для получения заказа с авторизацией"):
            response = requests.get(Const.GET_ORDER, headers=headers, json=payload)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 200
            assert MessageText.GET_ORDER in response.text

    @allure.title('Проверка получения заказа конкретного пользователя без авторизации')
    def test_get_order_without_authorization(self):
        headers = {"Content-type": "application/json"}

        with allure.step("GET-запрос для получения заказа без авторизации"):
            response = requests.get(Const.GET_ORDER, headers=headers)

        with allure.step("Проверяем статус код и ответ"):
            assert response.status_code == 401
            assert MessageText.GET_ORDER_WITHOUT_AUTH in response.text