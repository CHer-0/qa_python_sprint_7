import allure
import pytest
import requests
import links
import data


class TestMakeOrder:

    @allure.title(
        'Проверка создания заказов с разными вариантами цвета и возвращения их id в теле ответа в тэге "track"')
    @pytest.mark.parametrize('payload', data.payload_make_order())
    def test_make_order_any_color(self, payload):
        response = requests.post(links.EndPoints.EP_ORDER, data=payload)
        assert response.status_code == 201 and 'track' in response.json(), f'response.status_code == {response.status_code} and response.json() == {response.json()}'

    @allure.title(
        'Проверка что в тело ответа возвращается список заказов.')
    def test_orders_in_list(self, params=data.params_orders()):
        response = requests.get(links.EndPoints.EP_ORDER + params)
        assert response.status_code == 200 and type(response.json()["orders"]) == list, f'response.status_code == {response.status_code} and response.json()["orders"] == {response.json()["orders"]}'
