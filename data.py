from faker import Faker


BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'
URL_REGISTRATION = BASE_URL + 'regiatration/'

# Start page
TITLE = 'React App'
ERROR_MESSAGE_EMAIL_FIELD = 'Ошибка'

## Expected user name in header
USER_NAME = 'User.'


class User:
    
    def __init__(self):
        self.faker = Faker()
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
