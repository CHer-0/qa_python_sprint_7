import allure
import pytest
import links
import data
import requests


@allure.step('Создаем новую учетную запись курьера, возвращаем ее ID и по окончании теста ее удаляем')
@pytest.fixture()
def courier():
    payload = data.payload_create_same_courier()
    requests.post(links.EndPoints.EP_COURIER, data=payload)
    payload = data.payload_login_exist_courier()
    courier = requests.post(links.EndPoints.EP_LOGIN, data=payload).json()["id"]
    yield courier
    requests.delete(f'{links.EndPoints.EP_COURIER}/{courier}')
