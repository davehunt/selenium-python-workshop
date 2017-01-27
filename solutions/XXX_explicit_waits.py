import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def base_url():
    return 'https://the-internet.herokuapp.com'


@pytest.mark.nondestructive
def test_login(base_url, selenium):
    selenium.get('{0}/login'.format(base_url))
    selenium.find_element(By.ID, 'username').send_keys('tomsmith')
    selenium.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    selenium.find_element(By.CSS_SELECTOR, '#login button').click()
    WebDriverWait(selenium, timeout=5).until(
        expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR, '.example .button')))
    heading = selenium.find_element(By.CSS_SELECTOR, '.example h2')
    assert heading.text == 'Secure Area'
