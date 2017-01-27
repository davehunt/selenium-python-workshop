1. Run tests using SauceLabs: `pytest -n auto --driver SauceLabs --variables solutions/variables.json --capability browserName firefox solutions/XXX_page_objects.py`

2. Modify `solutions/variables.json` to cause login failures and run the tests again: `pytest -n auto --driver SauceLabs --variables solutions/variables.json --capability browserName firefox --html results.html solutions/XXX_page_objects.py`

3. Show the enhanced HTML report with videos and links to Sauce Labs jobs: `open results.html`

4. Run tests using BrowserStack: `pytest -n auto --driver BrowserStack --variables solutions/variables.json --capability browserName firefox --html results.html solutions/XXX_page_objects.py`

5. Show the enhanced HTML report: `open results.html`

6. Run tests using TestingBot: `pytest -n auto --driver TestingBot --variables solutions/variables.json --capability browserName firefox --html results.html solutions/XXX_page_objects.py`

7. Show the enhanced HTML report: `open results.html`

8. Run tests using CrossBrowserTesting: `pytest -n auto --driver CrossBrowserTesting --variables solutions/variables.json --capability browserName firefox --capability browser_api_name FF46 --capability os_api_name Win10 --html results.html solutions/XXX_page_objects.py`

9. Show the enhanced HTML report: `open results.html`
