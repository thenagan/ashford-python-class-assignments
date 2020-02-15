# initalize empty list to collect employee information
Employee1 = []

# initalize employee ssn search
EmployeeSSN = 0

# global variable to save index of found record
Employee_Index = 0

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
        print("\n Information has successfully added to system\n")
        print("---------------------------------------------")
        try:
            option = input('''Enter q to quit or anything else to return to Main Menu ''')
            if option.lower() == 'q':
                cls()
            else:
                cls()
                addEmployeeToList()
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
    print("4. Edit Employee information \n")
    print("5. Export employees information into text file \n ")
    print("6. Import employees information from a text file")
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

# Function to search for similar ssns.
def ssnsearch(edit):
    cls()
    print("-----------------------------------------------------\n")
    print("               Search Employee by SSN \n")
    print("-----------------------------------------------------\n")
    if (len(Employee1) == 0):
        input(" There is no employees in the system. \n")
        cls()
    else:
        try:
            ssn = input("Enter Q/q to exit or enter a new employee SSN ")
            global EmployeeSSN
            EmployeeSSN = ssn
            if ssn.lower() == "q":
                return 0
        except ValueError:
            ssnsearch(0)

        for i in range(0, len(Employee1)):
            line = Employee1[i].split(',')
            if line[1] == ssn:
                global Employee_Index
                Employee_Index = i
                employee_Info(line[0], line[1], line[2], line[3], line[4])
                break
            else:
                print("    Can not find a Employee with that SSN \n")
                return 0
    try:
        if (edit == 0):
            option = input("Enter q/Q to exit or anything to search for another employee")
            if option.lower() == 'q':
                cls()
            else:
                ssnsearch(0)
    except:
        cls()


# Edit function to have the user edit employee information
def edit():
    cls()
    result = ssnsearch(1)
    if result != 0:
        name = input('Enter New Employee Name: ')
        ssn = input('Enter New Employee SSN: ')
        phone = input('Enter New Employee Phone No.: ')
        PhoneNum4 = phone[:3]+"-"+phone[3:6]+'-'+phone[6:10]
        email = input('Enter New Employee Email: ')
        salary = input('Enter New Employee Salary: ')
        # Deleting old information to add new information
        del Employee1[Employee_Index]
        line = name +',' +ssn +',' +PhoneNum4 +',' +email +',' +salary
        # Adding new inserted information
        Employee1.insert(Employee_Index, line)
        input('''information has been Updated, press anything to return
        to Main Menu''')


# Function for Importing employee information
def getfile():

# open with argument as file name and infile as variable for loop
    with open("employee.txt") as infile:
        Employee1.extend(infile.read().splitlines())
        infile.close()
        print("You have imported: \n", Employee1)
# Funciton for Exporting employee information
def storecontent():
    # write line with line breaks in between, which will join lines
    # and write the string that is created directly to the file
    # the with open syntax automatically closes file at end of block
    with open("employee.txt", 'w') as myfile:
    # use myfile as variable for iteration
        # iterate over each line in text creating it in newline for file
        for lines in Employee1:
            myfile.write(lines)
            myfile.write('\n')
        myfile.close()
        print('Exported successfully')

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
        cls()
        ssnsearch(0)
    # Edit employee information
    if mode == 4:
        cls()
        edit()
    # Export Employee information to text file
    if mode == 5:
        cls()
        storecontent()
    # Import employee information from text file
    if mode == 6:
        cls()
        getfile()
