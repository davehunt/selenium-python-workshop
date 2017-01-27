from pypom import Page
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope='session')
def base_url():
    return 'https://the-internet.herokuapp.com'


class Base(Page):
    _error_locator = (By.CSS_SELECTOR, '#flash.error')
    _heading_locator = (By.CSS_SELECTOR, '.example h2')

    @property
    def error(self):
        return self.find_element(*self._error_locator).text

    @property
    def heading(self):
        return self.find_element(*self._heading_locator).text


class Login(Base):
    URL_TEMPLATE = '/login'
    _username_locator = (By.ID, 'username')
    _password_locator = (By.ID, 'password')
    _login_locator = (By.CSS_SELECTOR, '#login button')

    def wait_for_page_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            self._login_locator))
        return self

    def login(self, username, password, error=False):
        self.find_element(*self._username_locator).send_keys(username)
        self.find_element(*self._password_locator).send_keys(password)
        self.find_element(*self._login_locator).click()
        if error:
            return self.wait.until(lambda _: self.error)
        return Secure(self.selenium, self.base_url).wait_for_page_to_load()


class Secure(Base):
    _logout_locator = (By.CSS_SELECTOR, '.example .button')

    def wait_for_page_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            self._logout_locator))
        return self

    def logout(self):
        self.find_element(*self._logout_locator).click()
        return Login(self.selenium, self.base_url).wait_for_page_to_load()


@pytest.mark.nondestructive
def test_login(base_url, selenium, variables):
    page = Login(selenium, base_url).open()
    page.login(variables['username'], variables['password'])
    assert page.heading == 'Secure Area'


@pytest.mark.nondestructive
def test_logout(base_url, selenium, variables):
    page = Login(selenium, base_url).open()
    page = page.login(variables['username'], variables['password'])
    page = page.logout()
    assert page.heading == 'Login Page'


@pytest.mark.nondestructive
def test_invalid_login(base_url, selenium):
    page = Login(selenium, base_url).open()
    error = page.login('foo', 'bar', error=True)
    assert 'Your username is invalid' in error
