import hashlib
import getpass
from password_check import password_check
from email_check import email_check
from pwned_api import pwned_func

# User is asked to enter an email
email = input('Please enter your email: ')
# User is asked to enter a password
# getpass module hides users password input
password = getpass.getpass('Please enter your password: ')

# Running function for email check
email_check(email)
# Running function for password check
password_check(password)
# Running function that checks if your password was ever hacked
pwned_func(password)

# Password 256 encode, still needs work!

# password_ecode = password.encode()
# hsh = hashlib.sha256(password_ecode)
# pw_hsh = hsh.digest()
