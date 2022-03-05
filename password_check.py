import re
import getpass
from pwned_api import *

# Regular expression for password with at least 8 characters, upper case, numbers and at least one symbol
pattern_password = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#\$%])(?=.{8,})")


def password_check():
    while True:
        # User is asked to enter a password
        # getpass module hides users password input
        password = getpass.getpass('Please enter your password: ')
        # User input is compared with password pattern
        if pattern_password.match(password):
            print('You have entered a valid password, thank you!')
            pwned_api_check(password)
            pwned_func(password)
            break
        else:
            # If user doesn't provide a valid password he will be asked to enter a valid one
            print('Please enter a valid password!')
