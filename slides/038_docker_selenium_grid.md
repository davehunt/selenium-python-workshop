# Docker Selenium Grid
You can also use Docker to start a Selenium Grid hub and nodes. Each Docker container runs as a process on your host machine, so this isn't a way to massively scale, but it can be useful for supporting multiple browsers and running sessions in parallel.

# Exercise
1. Run a hub container: `docker run -d -P selenium/hub`
2. Determine the id of the container, and the port Selenium is running on: `docker ps`
3. Run three Firefox node containers: `docker run -d --link [id]:hub selenium/node-firefox`
4. Run the tests against the Docker container by using the `Remote` driver and the appropriate value for `--port`
5. Open the web console at  http://localhost:[port]/grid/console and see the nodes in use.
6. Kill the Docker containers: `docker kill [id]`
