# The bicycle for app "Доска".

## Acknowledgments

[The team of Yandex Practikum](https://github.com/yandex-praktikum)

Tomcat which gets up me early every morning.

## How to start

For testing we used libraries `pytest` (latest version), `selenium` (ver. 3.141.0),  `chromedriver-autoinstaller` for autoinstalling `chromedriver` and `Faker` with ver.37.12.0 (the high version for python>=3.9).

**Note** The library selenium uses `urllib3` with the version `1.26.16`.

1. Create a virtual environment (`venv`)

   ```bash
    py -3.13 -m venv venv
   ```

   Or

   ```bash
    python -m venv venv
   ```

2. Activate the venv

    ```bash
    source venv/Scripts/activate
    ```

3. Install libraries by `requirements.txt`

    ```bash
    pip install -r requirements.txt
    ```

4. Start tests

    ```bash
    pytest
    ```

    **Note** Use the key `-v` to show a verbose report.

## Which tests could have been used

1. Регистрация пользователя.
    - Steps:
      1. Press the button «Вход и регистрация».
      2. Press the button «Нет аккаунта».
      3. Fill all fields up.
      4. Press the button «Создать аккаунт».
    - Check:
      1. Redirect to the main page app.
      2. On the right corner near the button «Разместить объявление»
         display a user avatar and a the name `User`.

2. Регистрация пользователя c email не по маске  `*******@*******.***`.
    - Steps:
      1. Press the button «Вход и регистрация».
      2. Press the button «Нет аккаунта».
      3. Fill the email field up with incorrect data.
      4. Press the button «Создать аккаунт».
    - Check:
    The fields `Email`, `Пароль`, `Повторите пароль` are marked by
    red color and under the field `Email` showed up the message `Ошибка`.

3. Регистрация уже существующего пользователя.
    - Steps:
      1. Press the button «Вход и регистрация».
      2. Press the button «Нет аккаунта».
      3. Fill the fields up with existent user data.
      4. Press the button «Создать аккаунт».
    - Check:
    The fields `Email`, `Пароль`, `Повторите пароль` are marked by
    red color and under the field `Email` showed up the message `Ошибка`.

4. Login пользователя.
    - Steps:
      1. Press the button «Вход и регистрация».
      2. Fill the fields up with existent user data.
      3. Press the button «Войти».
    - Check:
      1. Redirect to the main page app.
      2. On the right corner near the button «Разместить объявление»
          display a user avatar and a the name `User`.

5. Logout пользователя.
    - Steps:
      1. Press the button «Вход и регистрация».
      2. Fill the fields up with existent user data.
      3. Press the button «Войти».
      4. Press the button «Выйти».
    - Check:
      1. On the right corner near the button «Разместить объявление»
          don't display a user avatar and a the name `User`.
      2. On the right corner near the button «Разместить объявление»
          display the button «Вход и регистрация».

6. Создание объявления неавторизованным пользователем.
    - Steps:
      1. Press the button «Разместить объявление».
    - Check:
    The title «Чтобы разместить объявление, авторизуйтесь» is show up.

7. Создание объявления авторизованным пользователем.
    - Steps:
      1. Sign in by an existence user.
      2. Fill an announcement up:
          name, description, price, categories, city, choose.
      3. Choose 'new' or 'used'.
      4. Press publish.
    - Check:
    The name, the city and the price have expected values.

## Miscellenious
1. [Faker docs](https://faker.readthedocs.io/en/master/)
