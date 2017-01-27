# Using the Selenium server
When using the Selenium server, all commands are sent across the network to the machine running the standalone server, which then executes them locally.

## Exercise
1. Start a standalone server using `java -jar selenium-server-standalone-3.0.1.jar`
2. Run the tests against the server by using the `Remote` driver and `browserName` capability set to `firefox`
