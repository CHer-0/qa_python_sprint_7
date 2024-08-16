import allure
import pytest
import requests
import links
import data


class TestLoginCourier:

    @allure.title('Проверка успешного логина учетной записи курьера и возвращения его id в теле ответа')
    def test_create_new_courier(self, courier):
        response = requests.post(links.EndPoints.EP_LOGIN, data=data.payload_login_exist_courier())
        assert response.status_code == 200 and response.json()["id"] == courier, f'response.status_code == {response.status_code} and response.json()["id"] == {response.json()["id"]}'

    @allure.title(
        'Проверка логина учетной записи курьера без одного из обязательных реквизитов и возвращение соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize('payload', data.login_couriers_without_one_required_field())
    def test_create_new_courier_without_required_field(self, payload, courier):
        response = requests.post(links.EndPoints.EP_LOGIN, data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа", f'response.status_code == {response.status_code} and response.json()["message"] == {response.json()["message"]}'

    @allure.title(
        'Проверка логина учетной записи курьера с неправильным одним из обязательных реквизитов и возвращение соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize('payload', data.login_couriers_wrong_required_field())
    def test_create_new_courier_with_wrong_field(self, payload, courier):
        response = requests.post(links.EndPoints.EP_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена", f'response.status_code == {response.status_code} and response.json()["message"] == {response.json()["message"]}'
