import data


class TestStartPage:

    def test_start_page_is_available(self, driver):
        driver.get(data.BASE_URL)

        assert (driver.current_url == data.BASE_URL and 
                driver.title == data.TITLE)
