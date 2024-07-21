from faker import Faker

fake = Faker('ru_RU')


# генерируем случайный логин
def login_generate():
    login = fake.user_name()
    return login


# генерируем случайный пароль
def password_generate():
    password = fake.password(length = 10, special_chars = False, digits = False, upper_case = False, lower_case = True)
    return password


# генерируем случайное имя
def first_name_generate():
    first_name = fake.first_name()
    return first_name


# генерируем случайную фамилию
def last_name_generate():
    last_name = fake.last_name()
    return last_name


# генерируем случайный номер телефона
def phone_number_generate():
    phone_number = fake.phone_number()
    return phone_number


# генерируем случайный адрес
def address_generate():
    address = fake.street_address()
    return address
