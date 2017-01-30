1. Run a standalone server with Firefox: `docker run -d -P selenium/standalone-firefox`

2. Show all running Docker containers: `docker ps`

3. Show logs for a the container: `docker logs [id]`

4. Run the tests to demonstrate they pass without any windows popping up: `pytest -n auto --driver Remote --port [port] --variables solutions/variables.json --capability browserName firefox solutions/032_page_objects.py`

5. Kill the Docker container: `docker kill [id]`
