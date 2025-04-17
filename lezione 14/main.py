# # PyPI (Python Package Index)

# The Python Package Index (PyPI) is the official third-party software repository for Python. 
# It is a central platform where developers can publish and share Python packages, 
# making it easier for others to find and install them.

# ## Key Features of PyPI
# - **Package Hosting**: PyPI hosts thousands of Python libraries and tools.
# - **Dependency Management**: It allows users to manage dependencies for their Python projects.
# - **Versioning**: Supports multiple versions of the same package, enabling compatibility with 
# different Python versions and environments.
# - **Search and Discovery**: Provides a searchable index to find packages by name, keywords, or functionality.

# ## How to Use PyPI
# 1. **Installing Packages**: Use `pip`, the Python package manager, to install packages from PyPI.
#     ```bash
#     pip install <package-name>
#     ```
# 2. **Publishing Packages**: Developers can publish their own packages to PyPI 
# using tools like `setuptools` and `twine`.

# pip install requests==2.32.2 # This will install the specific version 2.32.2 of the requests library.
# pip show requests # This will show the details of the requests library, including its version.
# pip list # This will show all the installed libraries and their versions.
# pip freeze # This will show all the installed libraries and their versions in 
#   a format that can be used to recreate the environment.
# pip freeze > requirements.txt # This will create a requirements.txt file with all 
#   the installed libraries and their versions.
# pip install --upgrade requests # This will upgrade the requests library to the latest version.
# pip install -r requirements.txt # This will install all the libraries listed in the requirements.txt file.

# python -m venv api_calls_venv # This will create a virtual environment named api_calls_venv.
# ./api_calls_venv/Scripts/activate # This will activate the virtual environment on Windows.
# source api_calls_venv/bin/activate # This will activate the virtual environment on Linux/Mac.

import requests # for HTTP requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather") # This will send a GET request to the GitHub API.
try:    
    response.raise_for_status() # This will raise an HTTPError if the response was unsuccessful.
except HTTPError as e:
    print("Errore nella richiesta")
else:
    print(response.url) # prints the endpoint of the request
    print(response.text) # prints the response as a text
    print(response.json()) # prints the response as a json
    print(response.content) # prints the response as a binary

