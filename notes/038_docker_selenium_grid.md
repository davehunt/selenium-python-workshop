1. Run a hub container: `docker run -d -P selenium/hub`

2. Point out the container id and port Selenium is running on: `docker ps`

3. Show the web console: `open http://localhost:[port]/grid/console`

4. Run three Firefox node containers: `docker run -d --link [id]:hub selenium/node-firefox`

5. Point out the container ids and ports Selenium is running on: `docker ps`

6. Show the node logs to demonstrate successful connection to the hub: `docker log [id]`

7. Refresh the console to show the new nodes: `open http://localhost:[port]/grid/console`

8. Run the tests and refresh the console to show nodes in use: `pytest -n auto --driver Remote --port [port] --variables solutions/variables.json --capability browserName firefox solutions/XXX_page_objects.py`
