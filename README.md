# S202-grade-manager
Repository dedicated to storing the S202 - Database II project where a grading system is made using a non-relational database.

## Code Quality
### Linter
A linter that checks for syntax errors, potential bugs, and style violations.\
The project uses [flake8](https://flake8.pycqa.org/en/latest/) as linter. To run the linter all code, execute the following command:
```bash
flake8 .
```
If the linter find a problem, it will show a message with the error.
```bash
./src/example.py:13:3: E303 too many blank lines (2)
./src/example.py:20:1: W391 blank line at end of file
```
Fixing the error manually and when finish, flake8 will not show any message.

### Formatter
The project uses [black](https://black.readthedocs.io/en/stable/) as formatter. To run the formatter in all code, execute the following command:
```bash
black .
```

### Sorting Imports
The project uses [isort](https://pycqa.github.io/isort/) as sorting imports. To run the sorting imports in all code, execute the following command:
```bash
isort .
```
