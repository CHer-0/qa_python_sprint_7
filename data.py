import allure


@allure.step("подставим учетные данные нового тестового курьера")
def payload_login_exist_courier():
    return {
        "login": "kourier",
        "password": "1234"
    }


@allure.step("собираем тело запроса с уже созданными ранее учетными данными курьера")
def payload_create_same_courier():
    return {
        "login": "kourier",
        "password": "1234",
        "firstName": "CHEr-0"
    }


@allure.step("собираем тело запроса с поочередно пустым логином и паролем")
def login_couriers_without_one_required_field():
    payload1 = {
        "login": "",
        "password": 1234
    }
    payload2 = {
        "login": "kourier",
        "password": ""
    }
    payloads = [payload1, payload2]
    return payloads


@allure.step("собираем тело запроса с поочередно неправильным логином и паролем")
def login_couriers_wrong_required_field():
    payload1 = {
        "login": "wrong",
        "password": 1234
    }
    payload2 = {
        "login": "kourier",
        "password": "wrong"
    }
    payloads = [payload1, payload2]
    return payloads


@allure.step("собираем тело запроса с различными вариантами цвета")
def payload_make_order():
    payload1 = payload2 = payload3 = payload4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    payload2["color"] = ["GRAY"]
    payload3["color"] = ["BLACK", "GRAY"]
    payload4["color"] = []

    payloads = [payload1, payload2, payload3, payload4]
    return payloads


@allure.step("Зададим параметры отбора заказов (не более 10)")
def params_orders():
    limit = 10
    page = 0
    params = f'?limit={limit}&page={page}'
    return params
