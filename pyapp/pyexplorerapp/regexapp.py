from pyshared.regexutils.regexutilities import is_alpha_or_numberic
import os

# Get the value of the PYTHONPATH environment variable
pythonpath = os.environ.get('PYTHONPATH')

# Print the value of PYTHONPATH
print(f'PYTHONPATH: {pythonpath}')

alpha = "abcd"
print(alpha + " is " + str(is_alpha_or_numberic(alpha)))

numeric = "12345"
print(numeric + " is " + str(is_alpha_or_numberic(numeric)))

none_alpha_numeric = "abcd$12345"
print(none_alpha_numeric + " is " + str(is_alpha_or_numberic(none_alpha_numeric)))
