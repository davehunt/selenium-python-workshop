1. Open https://the-internet.herokuapp.com/login

2. Demonstrate using the web console to locate the username field using XPath: `$x("//*[@id='username']")`

3. Demonstrate using the web console to locate the login button using XPath: `$x("//*[@id='login']//button")`

4. Show that we could be less ambiguous with XPath, but this comes at a cost for readability: `$x("//*[contains(@class, 'fa-sign-in')]/parent::button")`
