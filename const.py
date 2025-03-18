class Const:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_URL}/api/auth/register'
    LOGIN_USER = f'{MAIN_URL}/api/auth/login'
    UPDATE_DATA = f'{MAIN_URL}/api/auth/user'
    CREATE_ORDER = f'{MAIN_URL}/api/orders'
    GET_ORDER = f'{MAIN_URL}/api/orders'

class MessageText:
    CREATE_USER = 'success":true'
    CREATE_USER_TWICE = 'User already exists'
    CREATE_COURIER_WITHOUT_PASSWORD = 'Email, password and name are required fields"'
    LOGIN_USER = '"success":true'
    INCORECT_LOGIN_DATA = 'email or password are incorrect'
    UPDATE_USER = 'success":true'
    UPDATE_USER_UNSUCCESSFULLY = '"You should be authorised"'
    CREATE_ORDER = 'success":true'
    CREATE_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    CREATE_ORDER_INCORRECT_INGTEDIENTS = 'Internal Server Error'
    GET_ORDER = 'success":true'
    GET_ORDER_WITHOUT_AUTH = 'You should be authorised'

class Ingredients:
    BUN = '61c0c5a71d1f82001bdaaa6d'
    SPICY_SAUSE = '61c0c5a71d1f82001bdaaa72'
    MEAT_PROTOSTOMIA = '61c0c5a71d1f82001bdaaa6f'
    INCORRECT_INGTEDIENTS = '61c0c5a71d1f82001bdaaa72invalid'
