# Execute this, then run flake8 and fix issues

import json
data = {'spam': 'ham'}  # eggs
for i in range(2):
    print(i, json.dumps(data))
