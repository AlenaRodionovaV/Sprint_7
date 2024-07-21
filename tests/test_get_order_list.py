import allure
import requests
from api.api_data_generator import login_generate, password_generate, first_name_generate
from api.api_responses import Responses
from api.api_urls import Urls


class TestGetOrderList:

    @allure.title('Проверка получения всего списка заказов')
    @allure.description('Проверяем, что можно получить список вообще всех заказов')
    def test_get_order_list(self):
        # отправляем запрос на получение всего списка заказов
        response = requests.get(Urls.order_issue_url)
        # проверяем статус ответа и наличие определенных параметров в ответе
        assert response.status_code == 200, 'availableStations' and 'orders' in response.json()

    @allure.title('Проверка получения списка заказов по id')
    @allure.description('Проверяем, что можно получить список активных и завершенных заказов по id курьера')
    def test_get_order_list_by_id(self):
        payload = {
            "login": login_generate(),
            "password": password_generate(),
            "firstName": first_name_generate()
        }

        # отправляем запрос на создание курьера
        requests.post(Urls.create_courier_url, data = payload)
        # отправляем запрос на авторизацию курьера
        login_response = requests.post(Urls.login_courier_url, data = payload)
        courier_id = login_response.json()['id']
        # отправляем запрос на получение списка заказов авторизованного курьера по id
        order_response = requests.get(f"{Urls.order_issue_url}?courierId={courier_id}")
        assert order_response.status_code == 200, 'orders' and 'pageInfo' and 'availableStations' in order_response.json()
        # постусловие: отправляем запрос на удаление курьера
        delete_courier_response = requests.delete(f"{Urls.delete_courier_url}/{courier_id}")
        assert delete_courier_response.status_code == 200, delete_courier_response.json() == Responses.success_delete_courier_text
