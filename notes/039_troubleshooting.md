1. Modify `solutions/variables.json` to cause login failures and run the tests with additional command line options: `pytest --driver Firefox --verbose -r apP --tb=long --showlocals solutions/032_page_objects.py`

2. Talk through the additional console output.

3. Run the tests again to focus on the first failure: `pytest --driver Firefox --last-failed -x --pdb solutions/032_page_objects.py`

4. Talk through using the Python debugger.
