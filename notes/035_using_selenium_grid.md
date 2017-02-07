1. Start a hub: `java -jar resources/selenium/selenium-server-standalone-3.0.1.jar -role hub -host localhost`

2. Start a node: `java -jar resources/selenium/selenium-server-standalone-3.0.1.jar -role node -host localhost`

3. Show the web console: http://localhost:4444/grid/console

4. Run tests against the grid: `pytest -n auto --driver Remote --variables solutions/variables.json --capability browserName firefox solutions/032_page_objects.py`
