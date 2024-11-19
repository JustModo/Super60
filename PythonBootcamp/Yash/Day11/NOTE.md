# Command List

pytest -v file_name.py
pytest -v file.py::function_name
pytest dir_name
pytest file_name. py
pytest -v py::function_name

# Naming Convention

# Functions/methods
test_<fucntion_name>

# Classes
Test<class_name>

# Possible outcomes of a test:
PASSED (.): The test has passed successfully
FAILED (F): The test has failed
SKIPPED (s): The test was skipped
XFAIL (x): The test was expected to fail, it ran and failed
XPASS (X): The test was marked with XFai1 but it ran and passed
ERROR (E): An error occurred while running the test

When conducting tests in pytest
GIVEN -> WHEN -> THEN

Subset                      Syntax
Single test method          pytest path/test_module.py::test_method
All tests in a Class        pytest path/test_module.py::TestClass
Single test function        pytest path/test_module.py::test_function
All tests in a module       pytest path/test_module.py
all test in a directory     pytest path
tests matching a keyword    pytest -k "pattern"

