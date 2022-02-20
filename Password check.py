import re

pattern_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern_password = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#\$%])(?=.{8,})")

while True:
    email = input('Please enter your email: ')

    if pattern_email.fullmatch(email):
        print('You have entered a valid email, thank you!')
        break
    else:
        print('Please enter a valid email!')

while True:
    password = input('Please enter your password: ')

    if pattern_password.match(password):
        print('You have entered a valid password, thank you!')
        break
    else:
        print('Please enter a valid password!')
