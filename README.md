# Getting starting with Selenium and Python
This repository contains the slides, notes, exercises, and solutions for the workshop. If you are attending this workshop and would like to follow along, please follow this guide to install the prerequisites.

## Python
This workshop has been designed for Python 3.6, and this is the version I recommend you install. It may be possible to follow along using legacy Python (2.7) or other versions.

You can download Python from https://www.python.org/downloads/, where you can also find installation instructions for your platform.

## Virtual environment
In order to avoid installing packages into your default site packages, you should create a virtual environment to work in. This will be covered in the workshop, however if you want to install the package dependencies ahead of time, you will need to create a virtual environment using the command `python -m venv .workshop`. The environment can then be activated using `source .workshop/bin/activate` and deactivated using `deactivate`.

## Alternative interactive shells
Whilst not a requirement, the workshop does cover the alternative interactive shells [bpython](https://bpython-interpreter.org/) and [IPython](http://ipython.org/). These can be installed using `pip install bpython` and `pip install ipython` respectively.

## Package dependencies
The following package dependencies are required and used at various points in the workshop. These can be installed using `pip install <package>` from within your virtual environment. Note that this is not an exhaustive list of dependencies, as these packages have their own required dependencies that will be installed alongside them.

* pytest-selenium
* tox
* cookiecutter

## Firefox
The workshop will focus on using Firefox, which can be downloaded and installed from https://www.mozilla.org/firefox/. It is recommended that you install the latest release to the default location.

## GeckoDriver
In order to automate Firefox, the latest GeckoDriver binary should be downloaded for your platform from https://github.com/mozilla/geckodriver/releases and placed into your system path. The following resources may help here:

* [How to edit your system path in Windows](http://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)
* [How to add a new path to PATH the right way on OS X](http://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/)
* [Understanding environment variables and the Unix path](https://cbednarski.com/articles/understanding-environment-variables-and-the-unix-path/)

## The Internet
Several exercises in this workshop require access to an example application known as [The Internet](https://the-internet.herokuapp.com/). If you have a connection to the actual internet then you should be fine, however workshops are notorious for having connection difficulties. Fortunately, you can [download The Internet](https://github.com/tourdedave/the-internet/archive/master.zip) and run it locally. See the [getting started](https://github.com/tourdedave/the-internet#getting-started) guide for how to start the application.

## Java Runtime Environment
The Selenium server requires a Java Runtime Environment, which can be downloaded and installed for your platform from https://java.com/en/download/.

## Selenium standalone server
The Selenium server will be used to demonstrate running tests remotely. This can be downloaded from http://www.seleniumhq.org/download/.

## Sauce Labs
Sign up for a free Sauce Labs trial at https://saucelabs.com/ to run tests against their service. You'll need your username and API key during the workshop.

## Docker
The workshop will cover running tests against Docker containers. For this you will need Docker installed for your platform, which you can get from https://www.docker.com/products/overview.

## Git
In the final part of the workshop, we'll cover how to get hold of the Selenium source code, build the Python client, and run the tests. This will require you to have the Git SCM tool for your platform, which you can download from https://git-scm.com/downloads.
