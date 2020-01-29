import sys

# Function
def getfile(text): # text argument will be the file name

# open with argument as file name and infile as variable for loop
    with open(text) as infile:
        line2 = infile.readline()
        # while loop to consistenly read lines til there are no more
        while line2:
            print(line)
# Call function with text file to write import from
getfile('employee.txt')
