# calculator with try, except
import sys # NameError: name sys is not defined if not import
first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
    if operation == '+':
        print(first_value + second_value)
    elif operation == '-':
        print(first_value - second_value)
    elif operation == '/':
        print(first_value / second_value)
    elif operation == '//':
        print(first_value // second_value)
    elif operation == '*':
        print(first_value * first_value)
    elif operation == '**':
        print(first_value ** first_value)
    else:
        print(f'Invalid operation {operation}')
except ValueError:
    print('Value is not a digit')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Correct')
finally:
    print('End')

