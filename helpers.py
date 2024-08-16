import random
import string
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("генерируем учетные данные нового тестового курьера")
def new_courier_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


@allure.step("генерируем учетные данные нового тестового курьера с поочередно пустыми логином и паролем")
def create_couriers_without_one_required_field():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload1 = {
        "login": "",
        "password": password,
        "firstName": first_name
    }
    payload2 = {
        "login": login,
        "password": "",
        "firstName": first_name
    }
    payloads = [payload1, payload2]
    return payloads
