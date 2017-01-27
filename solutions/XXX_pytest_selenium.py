def test_login(selenium):
    selenium.get('https://the-internet.herokuapp.com/login')
    selenium.find_element_by_id('username').send_keys('tomsmith')
    selenium.find_element_by_id('password').send_keys('SuperSecretPassword!')
    selenium.find_element_by_css_selector('#login button').click()
