# Docker Selenium server
Docker images for Selenium include everything you need to run your tests in a more consistent and less distracting way. You don't need to worry about installing or updating versions of Selenium, the browsers, or the browser drivers. Running on different host hardware and operating systems should not affect results. If your application is also running in Docker, network latency is minimised.

# Exercise
1. Run a standalone server with Firefox: `docker run -d -P selenium/standalone-firefox`
2. Show all running Docker containers: `docker ps`
3. Show logs for a the container: `docker logs [id]`
4. Run the tests against the Docker container by using the `Remote` driver and the appropriate value for `--port`
5. Kill the Docker container: `docker kill [id]`
