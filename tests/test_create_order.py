import allure
import requests

from const import Const, Ingredients, MessageText


class TestCreateOder():

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_authorization(self, get_token):
        token = get_token
        payload = {
            "ingredients": [Ingredients.BUN, Ingredients.MEAT_PROTOSTOMIA, Ingredients.SPICY_SAUSE]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.CREATE_ORDER in response.text

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": [Ingredients.BUN, Ingredients.MEAT_PROTOSTOMIA, Ingredients.SPICY_SAUSE]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert MessageText.CREATE_ORDER in response.text

    @allure.title('Проверка создания заказа без указания ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = {
            "ingredients": []
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 400
        assert MessageText.CREATE_ORDER_WITHOUT_INGREDIENTS in response.text

    @allure.title('Проверка создания заказа с указанием невалидного хеша ингредиента')
    def test_create_order_incorrect_ingredient(self):
        payload = {
            "ingredients": [Ingredients.BUN, Ingredients.MEAT_PROTOSTOMIA, Ingredients.INCORRECT_INGTEDIENTS]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Const.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 500
        assert MessageText.CREATE_ORDER_INCORRECT_INGTEDIENTS in response.text