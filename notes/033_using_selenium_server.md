1. Start the standalone server: `java -jar resources/selenium/selenium-server-standalone-3.4.0.jar`

2. Run tests against the server: `pytest -n auto --driver Remote --variables solutions/variables.json --capability browserName firefox solutions/032_page_objects.py`
