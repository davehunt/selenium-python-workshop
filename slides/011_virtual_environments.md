# Virtual environments
By default all Python packages will be installed in your global site packages. This makes it difficult to manage multiple projects with conflicting requirements. Also, you don't need elevated privileges to install packages in a virtual environment.

## Exercise
1. List global site packages: `pip list --format columns`
2. Create a virtual environment: `python -m venv .workshop`
3. Activate the new virtual environment: `source .workshop/bin/activate`
4. List environment packages: `pip list --format columns`
5. Install the workshop requirements: `pip install -r solutions/requirements.txt`
6. Deactivate the virtual environment: `deactivate`
