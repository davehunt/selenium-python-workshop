from selenium.webdriver import Firefox


def test_login():
    driver = Firefox()
    # open https://the-internet.herokuapp.com/login
    driver.find_element_by_id('username').send_keys('tomsmith')
    # enter a password of 'SuperSecretPassword!'
    driver.find_element_by_css_selector('#login button').click()
    # close Firefox
