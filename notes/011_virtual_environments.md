1. Remove the existing virtual environment: `rm -rf .workshop`

2. List global site packages: `pip list --format columns`

3. Create a virtual environment: `python -m venv .workshop`

4. Activate the new virtual environment: `source .workshop/bin/activate`

5. List environment packages: `pip list --format columns`

6. Install the workshop requirements: `pip install -r solutions/requirements.txt`

7. Deactivate the virtual environment: `deactivate`
