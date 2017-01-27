# pytest-variables
pytest-variables is a pytest plugin for passing variables to tests from a file. It supports several formats including JSON, and provides the variables in the form of a dictionary via the `variables` fixture. It can be useful you don't want to hard-code values or have them in your source code repository.

## Exercise
1. Create a `variables.json`
2. Add keys for `username` and `password`
3. Modify the test to use the `variables` fixture.
