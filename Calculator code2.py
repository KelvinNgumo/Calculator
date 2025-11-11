def Addition(a, b):
    return a + b

def subdcription(a, b):
    return a - b

def  multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 'Error! Division by zero.'
    else:
        return a / b

print('List of available operations:')
print('1. Addition (+)')
print('2. Subtraction (-)')
print('3. Multiplication (*)')
print('4. Division (/)')
print('5. Exit')

choice = int(input("Select an operation to perform"))

if choice == 5:
    print('Exiting the calculator. Goodbye!')

else:

    a = float(input("Enter First number:"))
    b = float(input("Enter Second number:"))

if choice == 1:
    print('Result:', Addition(a, b))

elif choice == 2:
    print('Result:', subdcription(a, b))

elif choice == 3:
    print('Result:', multiplication(a, b))

elif choice == 4:
    print('Result:', division(a, b))

else:
    print('Invalid Operator Selected')


    

