from selenium.webdriver import Firefox


def test_login():
    driver = Firefox()
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element_by_id('username').send_keys('tomsmith')
    driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
    driver.find_element_by_css_selector('#login button').click()
    driver.quit()
