import re

# Regular expression for email
pattern_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def email_check(email):
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

