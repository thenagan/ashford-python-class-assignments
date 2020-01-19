# Name is the variable for the user input of their Name
Name = str(input('Enter your name  '))
# employeeSSN is the variable for the user input of their Social Security Number
employeeSSN = int(input('Enter your Social Security Number '))
# Areacode is the variable assignment for the input of the users first three digits of their phone number
AreaCode = input('Enter your phone number, Three digit Area code first ')
# PhoneNum is the variable assignment for the input of the rest of the users phone number
PhoneNum = input('Enter the rest of your phone number please ')
# Email is the variable assignment for the users input for their email
Email = input('Enter your email ')
# Salary is the variable assignment for the user input of their Salary
Salary = input('Enter your salary ')
# This print line will print my dashes.  Line 14 will print dashes with the user inputted name
# All of my blank print statement print() are there for spacing and design.
print('-' * 16, end='')
print(Name, '-' * 8)
print('          ---------------------')
print()
# Line 20 will print the string 'SSN:' with the user input Social Security Number
print('          SSN:', employeeSSN)
print()
# The next line was a concatenation strategy that I used to be able to get a parenthes with the first 3 numbers of the users phone number
print('          Phone:', "("+AreaCode[:3]+")"+PhoneNum[:3]+'-'+PhoneNum[3:7])
print()
# Line 26 prints the string 'Email:' along with the user input of their email
print('          Email:', Email)
print()
# Line 29, prints the string 'Salary:' with the user input of their Salary. I used f-string to be able to get the $ where I wanted it
print(f"          Salary: ${Salary}")
print()
# Lines 32 and 33 are presented to print the dashes(-) for the design of the output
print('-' * 40)
print('         ---------------------')
