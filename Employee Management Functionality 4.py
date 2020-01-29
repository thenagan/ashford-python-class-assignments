# Importing regular expression module
import re

# initalize empty list to collect employee information
Employee1 = []

# clear IDLE window, this is to make program cleaner
def cls():
    print ("\n" * 50)

# Display the employee information in the required format
def employee_Info(name, ssn, PhoneNum4, email, salary):
    print("")
    print('--------------- {0:s} ----------------'.format(name))
    print('SSN: {0:s}'.format(ssn))
    print('Phone: {0:s}'.format(PhoneNum4))
    print('Email: {0:s}'.format(email))
    print('Salary: ${0:s}'.format(salary))
    print("---------------------------------------")
    print("")

# view all employees in system
def viewEmployeeInfo():
    cls()
    print("-------------------------------------------------------------------")
    print("")
    print("               View all employees in the System")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    if(len(Employee1)==0):
        # Message when no employee is in the system
        print("----------------------------------------------------")
        print("              No employee in the list.")
        print("----------------------------------------------------")
    else:
        # Display all employees in the system
        for i in range(0, len(Employee1)):
            line = Employee1[i].split(',')
            employee_Info(line[0], line[1], line[2], line[3], line[4])
    try:
        option = int(input('Enter 0 to exit or any key to continue: '))
        if option == 0:
            cls()
    except:
        cls()

# Add employee to system
def addEmployeeToList():
    cls()
    print("-------------------------------------------------------------------")
    print("")
    print("            Add Employee information")
    print("-------------------------------------------------------------------")
    print("")
    try:
        # allow users to enter the employee information
        name = input('Employee Name: ')
        ssn = input('Employee SSN: ')
        phone = input('Employee Phone No.: ')
        PhoneNum4 = phone[:3]+"-"+phone[3:6]+'-'+phone[6:10]
        email = input('Employee Email: ')
        salary = input('Employee Salary: ')
        line = name +',' +ssn +',' +PhoneNum4 +',' +email +',' +salary
        index = len(Employee1)
        Employee1.insert(index, line)
    except:
        cls()
        addEmployeeToList()
# display the system "main menu"
def printOptions():
    print("---------------- Employee Management System --------------\n")
    print('There are ( {0:2d}) ) employees in the system.'.format(len(Employee1)))
    print("\n----------------------------------------------------------")
    print("1. View all employees \n")
    print("2. Add new employee \n")
    print("3. Search Employee by SSN \n")
    # validate the user selection
    try:
        answer = int(input('Please enter your option number: '))
    except ValueError:
        print("Not a number")
        return 100
    print("")
    print("----------------------------------------------------")
    print("")
    return answer

# Function to search for similar ssns. Not correct
def ssnsearch():
    cls()
    ssn2 = input('Enter a Social Security number to search ')
    # split turns a string to a list
    ssn2.split()
    # This turns the ssn input to list to search later
    SSN_List = [int(nums) for nums in ssn2]
    # attempt reg ex
    ssnsearch2 = re.compile("\d")
    s = ssnsearch2.match(s2)
    if s == True:
        edit()
    elif s == False:
        exit()
# Edit function to have the user edit employee information *Not Correct*
def edit():
    edit_option = input('''What information would you like to edit, 1 for
    name, 2 for social security number, 3 for phone, 4 for email, 5 for Salary
    anything else to exit ''')
    while True:
        # add updated information to a new info list
        new_info = []
        if edit_option == 1:
            try:
                name = input('Employee Name: ')
                new_info.insert(name)
            except:
                break
        elif edit_option == 2:
            try:
                ssn3 = input('Employee SSN: ')
                new_info.insert(ssn3)
            except:
                break
        elif edit_option == 3:
            try:
                phone = input('Employee Phone No.: ')
                new_info.insert(ssn)
            except:
                break
        elif edit_option == 4:
            try:
                email = input('Employee Email: ')
                new_info.insert(email)
            except:
                break
        elif edit_option == 4:
            try:
                salary = input('Employee Salary: ')
                new_info.insert(salary)
            except:
                break
    cls()
    employee_Info()

# Options for the user at the main menu
while True:
    cls()
    mode = printOptions()
    # view all employees in the system
    if mode == 1:
        cls()
        viewEmployeeInfo()
    # add employees to system
    if mode == 2:
        cls()
        addEmployeeToList()
    # Search Employee by SSN
    if mode == 3:
        ssnsearch()
