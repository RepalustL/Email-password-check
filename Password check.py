import re
import hashlib
import getpass

# Regular expression for email
pattern_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# Regular expression for password with at least 8 characters, upper case, numbers and at least one symbol
pattern_password = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#\$%])(?=.{8,})")

while True:
    # User is asked to enter an email
    email = input('Please enter your email: ')
    # User input is compared with email pattern
    if pattern_email.fullmatch(email):
        print('You have entered a valid email, thank you!')
        break
    else:
        # If user doesn't provide n valid email he will be asked to enter a valid one
        print('Please enter a valid email!')

while True:
    # User is asked to enter a password
    # getpass module hides users password input
    password = getpass.getpass('Please enter your password: ')
    # User input is compared with password pattern
    if pattern_password.match(password):
        print('You have entered a valid password, thank you!')
        break
    else:
        # If user doesn't provide a valid password he will be asked to enter a valid one
        print('Please enter a valid password!')


# Password 256 encode, still needs work!
password_ecode = password.encode()
hsh = hashlib.sha256(password_ecode)
pw_hsh = hsh.digest()
