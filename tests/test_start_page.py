import data


class TestStartPage:

    def test_start_page_is_available(self, driver):
        driver.get(data.URL)

        assert driver.current_url == data.URL and driver.title == data.TITLE
