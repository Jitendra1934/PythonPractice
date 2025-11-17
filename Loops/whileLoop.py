def user_inpt():
    try:
        a = int(i)
        if a>0:
            print('positive number')
        elif a ==0:
            print('you entered zero')
        else:
            print('you entered negative number')
    except ValueError:
        print("stop the program")


i =""
while i != 'exit':
    i = input("Enter a number: \n")
    user_inpt()