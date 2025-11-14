def amstrong(n):
    temp=n
    s=0

    while n>0:
        r=n%10
        s=s+r*r*r
        n=n//10

    if s==temp:
        print(temp,'is a amstrong')
    else:
        print(temp,'is not a amstrong')

amstrong(143)
