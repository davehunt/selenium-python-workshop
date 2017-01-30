# Running tests in parallel
Starting a browser for each test and running them one after another is not particularly efficient. Unfortunately some tests might require there to be only one browser open at a time, and some browsers do not even support having multiple instances open. That said, whenever possible you should try to run tests in parallel.

## Exercise
1. Run tests in parallel using `-n auto`
