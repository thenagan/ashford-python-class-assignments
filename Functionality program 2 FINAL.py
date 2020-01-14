print('You are going to enter five employee information in the same sequence')

Name1 = str(input('Enter name employee '))

five_employees1 = []
five_employees1.append(Name1)

employeeSSN1 = int(input('Enter Social Security Number '))

five_employees1.append(employeeSSN1)

AreaCode = input('Enter phone number, Three digit Area code first ')

PhoneNum = input('Enter the rest of the phone number please ')

PhoneTogether1 = "("+AreaCode[:3]+")"+PhoneNum[:3]+'-'+PhoneNum[3:7]

five_employees1.append(PhoneTogether1)

Email1 = input('Enter Email ')

five_employees1.append(Email1)

Salary1 = input('Enter Salary ')

Salary16 = f'${Salary1}'



print('Enter another employees information ')

five_employees2 = []

Name2 = str(input('Enter name '))

five_employees2.append(Name2)

employeeSSN2 = int(input('Enter Social Security Number '))

five_employees2.append(employeeSSN2)

AreaCode2 = input('Enter phone number, Three digit Area code first ')

PhoneNum2 = input('Enter the rest of the phone number please ')

PhoneTogether2 = "("+AreaCode2[:3]+")"+PhoneNum2[:3]+'-'+PhoneNum2[3:7]

five_employees2.append(PhoneTogether2)

Email2 = input('Enter Email ')

five_employees2.append(Email2)

Salary2 = input('Enter Salary ')

Salary26 = f'${Salary2}'

five_employees2.append(Salary26)


print('Enter another employees information ')

Name3 = str(input('Enter name '))
five_employees3 = []

five_employees3.append(Name3)

employeeSSN3 = int(input('Enter Social Security Number '))

five_employees3.append(employeeSSN3)

AreaCode3 = input('Enter phone number, Three digit Area code first ')

PhoneNum3 = input('Enter the rest of the phone number please ')

PhoneTogether3 = "("+AreaCode3[:3]+")"+PhoneNum3[:3]+'-'+PhoneNum3[3:7]

five_employees3.append(PhoneTogether3)

Email3 = input('Enter Email ')

five_employees3.append(Email3)

Salary3 = input('Enter Salary ')

Salary36 = f'${Salary3}'

five_employees3.append(Salary36)


print('Input another employees information ')

Name4 = str(input('Enter name '))

five_employees4 = []
five_employees4.append(Name4)

employeeSSN4 = int(input('Enter Social Security Number '))
five_employees4.append(employeeSSN4)
AreaCode4 = input('Enter phone number, Three digit Area code first ')

PhoneNum4 = input('Enter the rest of the phone number please ')
PhoneTogether4 = "("+AreaCode4[:3]+")"+PhoneNum4[:3]+'-'+PhoneNum4[3:7]
five_employees4.append(PhoneTogether4)
Email4 = input('Enter Email ')
five_employees4.append(Email4)
Salary4 = input('Enter Salary ')
Salary46 = f'${Salary4}'
five_employees4.append(Salary46)


print('Input another employees information ')
five_employees5 = []
Name5 = str(input('Enter name '))
five_employees5.append(Name5)
employeeSSN5 = int(input('Enter Social Security Number '))
five_employees5.append(employeeSSN5)
AreaCode5 = input('Enter phone number, Three digit Area code first ')

PhoneNum5 = input('Enter the rest of the phone number please ')
PhoneTogether5 = "("+AreaCode5[:3]+")"+PhoneNum5[:3]+'-'+PhoneNum5[3:7]
five_employees5.append(PhoneTogether5)
Email5 = input('Enter Email ')
five_employees5.append(Email5)
Salary5 = input('Enter Salary ')
Salary56 = f'${Salary5}'
five_employees5.append(Salary56)

employee_select = int(input('''Enter a number 1 through 5 to recieve the
information of the employee of your choice 1 being the first employee. '''))


if employee_select == 1:
    print(*five_employees1, sep=",")
elif employee_select == 2:
    print(*five_employees2, sep=",")
elif employee_select == 3:
    print(*five_employees3, sep=",")
elif employee_select == 4:
    print(*five_employees4, sep=",")
elif employee_select == 5:
    print(*five_employees5, sep=',')
else: print('You did not enter a number 1 through five to recieve information')
