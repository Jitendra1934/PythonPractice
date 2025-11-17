def studentMarks(marks):
    if marks >= 90:
        print("You got A grade")
    elif marks >= 80 and marks <= 90:
        print("You got B grade")
    else:
        print("You got C grade")

marks = int(input("Enter your marks:\n"))
studentMarks(marks)