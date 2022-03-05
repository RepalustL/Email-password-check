from password_check import password_check
from email_check import email_check
from pwned_api import pwned_func


# Running function for email check
email_check()
# Running function for password check
password_check()
# Running function that checks if your password was ever hacked
pwned_func()

# Password 256 encode, still needs work!

# password_ecode = password.encode()
# hsh = hashlib.sha256(password_ecode)
# pw_hsh = hsh.digest()
