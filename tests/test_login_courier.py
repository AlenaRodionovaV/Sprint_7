import allure
import requests
from api.api_data_generator import login_generate, password_generate, first_name_generate
from api.api_responses import Responses
from api.api_urls import Urls


class TestLoginCourier:

    @allure.title('Проверка успешной атворизации курьера')
    @allure.description('Проверяем, что созданный курьер может успешно залогиниться')
    def test_login_courier_success(self):
        payload = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        # отправляем запрос на создание курьера
        requests.post(Urls.create_courier_url, data = payload)
        # отправляем запрос на авторизацию только что созданного курьера
        login_courier_response = requests.post(Urls.login_courier_url, data = payload)
        # проверяем статус ответа и наличие id в тексте ответа
        assert login_courier_response.status_code == 200, 'id' in login_courier_response.json()
        # постусловие: отправляем запрос на удаление курьера
        delete_courier_response = requests.delete(f"{Urls.delete_courier_url}/{login_courier_response.json()['id']}")
        assert delete_courier_response.status_code == 200, delete_courier_response.json() == Responses.success_delete_courier_text

    @allure.title('Проверка ошибки атворизации курьера из-за отсутствия логина')
    @allure.description('Проверяем, что невозможно авторизовать курьера без указания логина')
    def test_login_courier_failed_without_login(self):
        payload_for_create = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        payload_for_login = {
            "login": '',
            "password": payload_for_create["password"],
            "firstName": payload_for_create["firstName"]
        }
        # отправляем запрос на создание курьера
        requests.post(Urls.create_courier_url, data = payload_for_create)
        # отправляем запрос на авторизацию курьера без указания логина
        response = requests.post(Urls.login_courier_url, data = payload_for_login)
        # проверяем статус ответа и наличие ошибки "Недостаточно данных для создания учетной записи"
        assert response.status_code == 400, response.json() == Responses.login_courier_without_login_or_password_text

    @allure.title('Проверка ошибки атворизации курьера из-за отсутствия пароля')
    @allure.description('Проверяем, что невозможно авторизовать курьера без указания пароля')
    def test_login_courier_failed_without_password(self):
        payload_for_create = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        payload_for_login = {
            "login": payload_for_create["login"],
            "password": '',
            "firstName": payload_for_create["firstName"]
        }
        # отправляем запрос на создание курьера
        requests.post(Urls.create_courier_url, data = payload_for_create)
        # отправляем запрос на авторизацию курьера без указания пароля
        response = requests.post(Urls.login_courier_url, data = payload_for_login)
        # проверяем статус ответа и наличие ошибки "Недостаточно данных для создания учетной записи"
        assert response.status_code == 400, response.json() == Responses.login_courier_without_login_or_password_text

    @allure.title('Проверка ошибки авторизации несуществующего курьера')
    @allure.description('Проверяем, что невозможно авторизовать курьера при указании несуществующих логина и пароля')
    def test_login_courier_not_exist(self):
        payload = {
            "login": 'courierdoesnotexist235percent',
            "password": '123487yrgbf329734fhd9j182374bfcn293784bf',
            "firstName": 'courierdoesnotexist235percent'
        }

        # отправляем запрос на авторизацию курьера с несуществующими логином и паролем
        response = requests.post(Urls.login_courier_url, data = payload)
        # проверяем статус ответа и наличие ошибки "Этот логин уже используется"
        assert response.status_code == 404, response.json() == Responses.login_courier_not_exist

