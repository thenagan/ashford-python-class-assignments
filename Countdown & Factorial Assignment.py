userNum = int(input('Enter a number greater than 1 '))
while userNum < 1:
    userNum = int(input('Enter a number greater than 1 please '))
userNum2 = int(input('''Enter 1 for the countdown of your number and 2 for
the factorial of that number '''))
while userNum2 not in range(1,3):
    userNum2 = int(input('''Please enter 1 or 2 for your option '''))
if userNum2 == 1:
    i = userNum
    for i in reversed(range(i)):
        print(i)
elif userNum2 == 2:
    factorial = 1
    for i in range(1, userNum + 1):
        factorial = factorial * i
    print(factorial)
