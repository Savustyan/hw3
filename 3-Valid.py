# EMAIL AND PASSWORD VALIDATOR
email: str = input('Input email: ')
password: str = input('Enter password: ')
# Classes for raise names
class LengthError(Exception):
    pass
class DigitError(Exception):
    pass
class LetterError(Exception):
    pass
class UppercaseError(Exception):
    pass
class LowercaseError(Exception):
    pass
class InvalidError(Exception):
    pass

try:
# Email
    if '@' not in email:
        raise InvalidError
    elif '.' not in email:
        raise InvalidError
    at_sign_index = email.index('@')
    for sign in {'.', '@'}:
        if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
            raise InvalidError
        elif email[-1] == sign or email[0] == sign:
            raise InvalidError
    else:
        print('Email is OK')
# Password
    if len(password) < 8 or len(password) > 128:
        raise LengthError
    elif password.isalpha():
        raise DigitError
    elif password.isdigit():
        raise LetterError
    elif password.islower():
        raise UppercaseError
    elif password.isupper():
        raise LowercaseError
    else:
        print('Password is OK')
except LengthError:
    print('Password is too short or long')
except DigitError:
    print('Password should contains digits')
except LetterError:
    print('Password should contains letters')
except UppercaseError:
    print('Password should contains uppercase letters')
except LowercaseError:
    print('Password should contains lowercase letters')
except InvalidError:
    print('Invalid email')
finally:
    print('CLOSE!')

