# PEP 8 - Python Enhancement Proposal

"""
- Naming Conventions
    - Use descriptive names
    - to name functions, use verbs for actions (e.g. calculate_total, send_email)
    - Use snake_case for variables and functions, PascalCase for classes, ALL_CAPS for constants
- Whitespaces:
    - Avoid excessive whitespaces in expressions and statements
    - Place a single space around operators and after commas
- Comments:
    - Write inline comments on the same line as the statement they refer to
    - Use comments to explain why something is done, not what is done
    - Don't rely on comments to clarify poorly written code
- Docstrings:
    - Use docstrings to explain and document a specific block of code, such as functions and classes. 

2 tools for helping us to format correctly:
- Linters - more complex, also check a bit for bugs
- Autoformatters

One of the best tools is Ruff, both a linter and an autoformatter
"""

# Typing "import this" we'll get some more of info known as "the zen of python"
import this

# These syntax means that the parameter should be a string, and that it should return a string
def test_function(name: str) -> str:
    return name

# flake8 is a tool that finds formatting problems in our code
# we need to type flake8 .\path to use it in the terminal

# autopep8 is a tool that fixes the script using pep8 guidelines automatically
# writing autopep8 --in-place .\path modifies the script directly

"if a string is too long like this one that i am writing here \
    (more than 79 characters), we can split it using the backslash"

# another tool is ruff
# we can write ruff check .\path --select ALL

# git config --global user.name "Your Name"
# git config --global user.email "Your Email"

# After navigating to the project folder we can run "git init"

# git log lists the latest changes

# git diff shows the differences between current and next file
# git checkout to change branch

