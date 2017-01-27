import pytest


@pytest.fixture(scope='session')
def base_url():
    return 'https://the-internet.herokuapp.com'


@pytest.mark.nondestructive
def test_login(base_url, selenium):
    selenium.get('{0}/login'.format(base_url))
    selenium.find_element_by_id('username').send_keys('tomsmith')
    selenium.find_element_by_id('password').send_keys('SuperSecretPassword!')
    selenium.find_element_by_css_selector('#login button').click()
