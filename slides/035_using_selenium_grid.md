# Using Selenium Grid
Selenium Grid is multiple standalone servers, where one takes the role of the hub, and others as nodes. The nodes register themselves to the hub, with details of the capabilities they support. When a new session request is sent to the hub, a matching node is picked, and the commands are proxied to that node.

## Exercise
1. Start a hub using `java -jar resources/selenium-server-standalone-3.0.1.jar -role hub`
2. Start a node using `java -jar resources/selenium-server-standalone-3.0.1.jar -role node`
3. Open the web console at http://localhost:4444/grid/console
4. Run the tests as with the Selenium server.
