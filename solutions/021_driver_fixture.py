import pytest
from selenium.webdriver import Firefox


@pytest.fixture(scope='function')
def driver():
    driver = Firefox()
    yield driver
    driver.quit()


def test_login(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element_by_id('username').send_keys('tomsmith')
    driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
    driver.find_element_by_css_selector('#login button').click()
