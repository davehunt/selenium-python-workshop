# Destructive tests
pytest-selenium is paranoid by default. It assumes that all tests are destructive, and that all URLs are sensitive. This means that you need to explicitly mark tests as non-destructive, and URLs are non-sensitive.

A destructive test is one that may leave an impact, such as adding, updating, or deleting data.

A sensitive URL is one that you do not under any circumstances want to run destructive tests on.
