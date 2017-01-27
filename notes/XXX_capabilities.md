1. Demonstrate launching Firefox in private browsing mode using capabilities.

```python
import pytest
@pytest.fixture
def capabilities(capabilities):
    capabilities['moz:firefoxOptions'] = {
        'args': ['--private']}
    return capabilities
```

2. Demonstrate simplifying this by using an Options object:

```python
import pytest
@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('--private')
    return firefox_options
```
