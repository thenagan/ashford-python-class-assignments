
print('''Welcome to the Employee system you are able to enter employee
information to add to the database, you will also be able to view employees
information by their name''')

Name1 = []

Employee1 = []

counter = 0

while counter <= 3:
    print("------------------------------------------------------\n")
    print('                  Number of Employees in System ({0:d})'.format(counter))
    print("------------------------------------------------------\n")
                # Allow users to enter employees name, ssn, phone, email and salary
    Name = input('Enter employee name: ')
                    # Add employee to Name list
    Name1.insert(counter, Name)
    SSN = input('Enter employee SSN: ')
    PhoneNum = input('Enter employee Phone Number ')
    PhoneNum4 = "("+PhoneNum[:3]+")"+PhoneNum[3:6]+'-'+PhoneNum[6:10]
    Email = input('Enter employee email ')
    Salary = input('Enter employee Salary: $ ')
    print("")
    print("")
    # Display will display employee information to user \ for more lines to use
    display = ('Name: ' +Name +'\n' +'SSN: '+SSN +'\n' +'Phone: ' +PhoneNum4 \
     +'\n' +'Email: ' +Email +'\n' +'Salary: ' +'$' +Salary)

                    # Add to employee list
    Employee1.insert(counter, display)
                    # increase count of employees in system by 1
    counter += 1
    # Displaying the number of employees in system to let the user know
    print("------------------------------------------------------\n")
    print('                  Number of Employees in System ({0:d})'.format(counter))
    print("------------------------------------------------------\n")
    # User input question to enter another employee or view employee question
    userview = (int(input('''Enter 1 to be able to view information of employees
     in the system, 2 to add another employee ''')))
    if userview == 1 or counter == 3:
        break
    elif userview == 2:
        continue
# After break, prompt will display how many employees are in the system
print("------------------------------------------------------\n")
print('                  Number of Employees in System ({0:d})'.format(counter))
print("------------------------------------------------------\n")

ques = int(input('''You entered the maximum number of employees, or
you want to view employee information that is in the system
enter 1 to view employees in system or 2 to exit the system \n\n '''))
print()
while ques == 1 or 2:
    if ques == 1:
        for i in Employee1:
            print(i, '\n')
        break
    elif ques == 2:
        exit()
# Print employee information that is in the system and print a goodbye message
print('''The information for the employees in the system are displayed
on the screen''')
print("Have a lovely rest of your day at work")
