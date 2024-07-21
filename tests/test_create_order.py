import allure
import pytest
import requests
from api.api_supportive_data import payload_both_color, payload_none_color, payload_black_color, payload_grey_color
from api.api_urls import Urls


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа при указании разных цветов самоката')
    @allure.description('Проверяем, что при оформлении заказа можно указать любой цвет или не указывать совсем')
    @pytest.mark.parametrize('payload', [payload_black_color, payload_grey_color, payload_none_color, payload_both_color])
    def test_create_order_with_diff_colors_success(self, payload):
        # отправляем запрос на оформление заказа с разными вариациями цветов самоката
        response = requests.post(Urls.order_issue_url, json = payload)
        # проверяем статус ответа и наличие номера заказа 'track' в ответе
        assert response.status_code == 201,  'track' in response.json()
