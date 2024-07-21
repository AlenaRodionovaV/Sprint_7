from api.api_data_generator import last_name_generate, address_generate, phone_number_generate, first_name_generate, \
    password_generate, login_generate

# данные для проверки возможности заказа самоката обоих цветов
payload_both_color = {
    "firstName": first_name_generate(),
    "lastName": last_name_generate(),
    "address": address_generate(),
    "metroStation": 2,
    "phone": phone_number_generate(),
    "rentTime": 4,
    "deliveryDate": "2024-08-15",
    "comment": "с ветерком",
    "color": [
        "BLACK",
        "GREY"
    ]
}

# данные для проверки возможности заказа самоката без указания цвета
payload_none_color = {
    "firstName": first_name_generate(),
    "lastName": last_name_generate(),
    "address": address_generate(),
    "metroStation": 3,
    "phone": phone_number_generate(),
    "rentTime": 6,
    "deliveryDate": "2024-08-11",
    "comment": "yiyi",
    "color": []
}

# данные для проверки возможности заказа самоката черного цвета
payload_black_color = {
    "firstName": first_name_generate(),
    "lastName": last_name_generate(),
    "address": address_generate(),
    "metroStation": 2,
    "phone": phone_number_generate(),
    "rentTime": 4,
    "deliveryDate": "2024-07-28",
    "comment": "-",
    "color": [
        "BLACK"
    ]
}

# данные для проверки возможности заказа самоката серого цвета
payload_grey_color = {
    "firstName": first_name_generate(),
    "lastName": last_name_generate(),
    "address": address_generate(),
    "metroStation": 2,
    "phone": phone_number_generate(),
    "rentTime": 4,
    "deliveryDate": "2024-07-28",
    "comment": "zzz",
    "color": [
        "GREY"
    ]
}

payload_without_password = {
    "login": login_generate(),
    "password": '',
    "firstName": first_name_generate()
}

payload_without_login = {
    "login": '',
    "password": password_generate(),
    "firstName": first_name_generate()
}
