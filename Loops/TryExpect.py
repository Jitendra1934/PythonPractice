a = input("Enter a number:\n ")

try:
    b = int(a)
    if b>0:
        print('positive number')
    else:
        print('negative number')
except ValueError:
    print('not a valid number ')