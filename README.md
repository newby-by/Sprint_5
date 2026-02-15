# The bicycle for app "Доска".

## Acknowledgments

[The team of Yandex Practikum](https://github.com/yandex-praktikum)

Tomcat which gets up me early every morning.

## How to start

For testing we used libraries `pytest` (latest version), `selenium` (ver. 3.141.0).

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
