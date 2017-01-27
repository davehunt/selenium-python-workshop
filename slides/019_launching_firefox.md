# Launching Firefox
With Firefox installed in the default location, and GeckoDriver available on the system path, launching Firefox from Selenium is simply:

```python
from selenium.webdriver import Firefox
driver = Firefox()
```

## Exercise
1. Launch Firefox from the Python interactive shell.
2. Use the `get` method to open https://the-internet.herokuapp.com/
3. Use `quit` to close Firefox.
