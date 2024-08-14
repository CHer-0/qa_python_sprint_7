import allure
import pytest
import requests
import links
import helpers
import data


class TestCreateCourier:

    @allure.title('Проверка успешного создания новой учетной записи курьера и возвращения соответствующего сообщения и статуса в теле ответа')
    def test_create_new_courier(self):
        payload = helpers.new_courier_payload()
        response = requests.post(links.EndPoints.EP_COURIER, data=payload)
        assert response.status_code == 201 and response.json()["ok"], f'response.status_code == {response.status_code} and response.json()["ok"] == {response.json()["ok"]}'

    @allure.title('Проверка создания уже созданной учетной записи курьера и возвращения соответствующей ошибки в теле ответа')
    def test_create_same_courier(self, courier):
        payload = data.payload_create_same_courier()
        response = requests.post(links.EndPoints.EP_COURIER, data=payload)
        assert response.status_code == 409 and response.json()[
            "message"] == "Этот логин уже используется. Попробуйте другой.", f'response.status_code == {response.status_code} and response.json()["message"] == {response.json()["message"]}'

    @allure.title('Проверка создания новой учетной записи курьера без одного из обязательных реквизитов и возвращения соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize("payload", helpers.create_couriers_without_one_required_field())
    def test_create_courier_without_required_field(self, payload):
        response = requests.post(links.EndPoints.EP_COURIER, data=payload)
        assert response.status_code == 400 and response.json()[
            "message"] == "Недостаточно данных для создания учетной записи", f'response.status_code == {response.status_code} and response.json()["message"] == {response.json()["message"]}'
