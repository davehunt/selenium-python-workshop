# Tox
Tox (http://tox.readthedocs.io/) is a tool for packaging, testing, and releasing Python software. Even though you're probably not going to package or release your tests, Tox can still be useful for running them. Rather than creating a virtual environment and installing your test dependencies manually, Tox can manage this for you. If you want, Tox can also run your tests against multiple Python versions, and can also take care of running flake8 or other tools.

# Exercise
1. Deactivate any active virtual environment.
2. Run Tox using `tox -c solutions/tox.ini`
3. Limit to a single environment by using `-e`
4. Run the tests in verbose mode using `--` to pass a positional argument.
