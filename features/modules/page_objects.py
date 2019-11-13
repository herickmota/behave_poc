from selenium.webdriver.common.keys import Keys


class Google:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com'
        self.navigate()

    @property
    def search_bar(self):
        return self.driver.find_element_by_name('q')

    def navigate(self):
        self.driver.get(self.url)

    def search(self, value):
        self.search_bar.clear()
        self.search_bar.send_keys(value)
        self.search_bar.send_keys(Keys.RETURN)

    def check_search(self, value):
        assert value, self.driver.title()
