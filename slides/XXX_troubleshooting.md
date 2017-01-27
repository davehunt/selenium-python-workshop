# Troubleshooting
When failures happen, the tracebacks can be a little difficult to read. Also, the tests run so fast that it's hard to visually see when something has gone wrong. In addition to the HTML report, there are a number of ways to help troubleshoot failures.

* `--verbose` will show details of each test.
* `-r apP` shows extra test summary for all tests.
* `--tb=long` shows a full traceback.
* `--showlocals` shows locals in tracebacks.
* `--last-failed` will only run the tests that previously failed.
* `-x` stops running the tests on the first failure.
* `--pdb` enters the Python debugger on failure.

If you have a test that fails intermittently, you can install the pytest-repeat plugin and combine `-x` with `--count=100` to repeat the test up to 100 times, but stop when a failure occurs.

# Exercise
Try some of these command line options. You can combine them to make troubleshooting even easier.
