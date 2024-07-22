import allure
import pytest
import requests
from api.api_data_generator import login_generate, password_generate, first_name_generate
from api.api_responses import Responses
from api.api_supportive_data import payload_without_login, payload_without_password
from api.api_urls import Urls


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверяем, что при отправке заполненных логина, пароля и имени создается курьер')
    def test_create_courier_success(self):
        payload = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        # отправляем запрос на создание курьера
        create_courier_response = requests.post(Urls.create_courier_url, data = payload)
        # проверяем статус ответа и наличие текста "ok": true
        assert create_courier_response.status_code == 201, create_courier_response.json() == Responses.success_create_courier_text
        # постусловие: отправляем запрос на авторизацию курьера для получения его id и удаляем курьера
        login_courier_response = requests.post(Urls.login_courier_url, data = payload)
        delete_courier_response = requests.delete(f"{Urls.delete_courier_url}/{login_courier_response.json()['id']}")
        assert delete_courier_response.status_code == 200, delete_courier_response.json() == Responses.success_delete_courier_text

    @allure.title('Проверка ошибки создания курьера из-за отсутствия логина или пароля')
    @allure.description('Проверяем, что невозможно создать курьера без указания логина или пароля')
    @pytest.mark.parametrize('payload', [payload_without_login, payload_without_password])
    def test_create_courier_failed_without_login_or_password(self, payload):
        # отправляем запрос на создание курьера без указания логина или пароля
        create_courier_response = requests.post(Urls.create_courier_url, json = payload)
        # проверяем статус ответа и наличие ошибки "Недостаточно данных для создания учетной записи"
        assert create_courier_response.status_code == 400, create_courier_response.json() == Responses.create_courier_without_login_or_password_text

    @allure.title('Проверка ошибки создания курьера из-за наличия уже существующего такого курьера')
    @allure.description('Проверяем, что нельзя создать двух курьеров с одинаковыми данными')
    def test_create_courier_failed_already_exist(self):
        payload = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        # отправляем запрос на создание курьера
        requests.post(Urls.create_courier_url, data = payload)
        # отправляем запрос на создание такого же курьера с такими же данными, как у предыдущего
        create_courier_response = requests.post(Urls.create_courier_url, data = payload)
        # проверяем статус ответа и наличие ошибки "Этот логин уже используется"
        assert create_courier_response.status_code == 409, create_courier_response.json() == Responses.already_exist_courier_text
        # постусловие: отправляем запрос на авторизацию курьера для получения его id и удаляем курьера
        login_courier_response = requests.post(Urls.login_courier_url, data = payload)
        delete_courier_response = requests.delete(f"{Urls.delete_courier_url}/{login_courier_response.json()['id']}")
        assert delete_courier_response.status_code == 200, delete_courier_response.json() == Responses.success_delete_courier_text
