import random
from abc import ABC

from faker import Faker


class UrlsMestro:
    BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'


class AnnouncementFormData:
    CATEGORIES = {
        'Авто': 1,
        'Книги': 2,
        'Садоводство': 3,
        'Хобби': 4,
        'Технологии': 5,
    }

    CONDITION_GOODS = {
        'Новый': 1,
        'Б/У': 2,
    }

    CITIES = {
        'Москва': 1,
        'Санкт-Петербург': 2,
        'Новосибирск': 3,
        'Екатеринбург': 4,
        'Нижний Новгород': 5,
        'Казань': 6,
    }


class HomePageData:
    TITLE = 'React App'
    ERROR_MESSAGE_EMAIL_FIELD = 'Ошибка'
    ERROR_CLASS = 'input_inputError'
    USER_NAME = 'User.'


class Data(ABC):
    def __init__(self):
        self.faker = Faker()


class User(Data):

    def __init__(self):
        super().__init__()
        self._user = ...

    @property
    def user_with_correct_credentials(self):
        return (self.faker.unique.email(), self.faker.password())

    @property
    def user_with_incorrect_email(self):
        return (self.faker.unique.email() + "1", self.faker.password())

    @property
    def new(self):
        self._user = (self.faker.unique.email(), self.faker.password())
        return self._user

    @property
    def existent(self):
        return self._user


user = User()


class Announcement(Data):

    def __init__(self):
        super().__init__()
        self._name = self.faker.sentence()
        self._category = random.choice(list(AnnouncementFormData.CATEGORIES))
        self._condition = random.choice(
            list(AnnouncementFormData.CONDITION_GOODS)
        )
        self._city = random.choice(list(AnnouncementFormData.CITIES))
        self._description = self.faker.paragraph()
        self._price = self.faker.random_int(min=0, max=999)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def condition(self):
        return self._condition

    @property
    def city(self):
        return self._city

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price


expected_announcement = Announcement()
