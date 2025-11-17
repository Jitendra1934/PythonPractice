def ageCheck(bAge,gAge):
    if bAge>=21 and gAge>=18:
        print('Eligible for Wedding')
    else :
        print('Not eligible for Wedding')

b = int(input("Enter your boy age:\n "))
g = int(input("Enter your girl age:\n "))

ageCheck(b, g)
