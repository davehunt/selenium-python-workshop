1. Run the tests: `pytest --driver Firefox --html results.html solutions/030_pytest_variables.py`

2. Open the HTML report: `open results.html`

3. Modify `solutions/variables.json` to cause login failures and run the tests again: `pytest --driver Firefox --html results.html solutions/030_pytest_variables.py`

4. Open the new HTML report and talk through the differences: `open results.html`
