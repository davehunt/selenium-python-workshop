# List global site packages
pip list --format columns
# Create virtual environment
python -m venv .workshop
# Activate virtual environment
source .workshop/bin/activate
# List environment packages
pip list --format columns
# Deactivate virtual environment
deactivate
