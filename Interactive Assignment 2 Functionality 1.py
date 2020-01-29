# Not sure if I need this but importing it so I can access files in system
import sys
# Function name with text as argument.
def storecontent(text):
    # write line with line breaks in between, which will join lines
    # and write the string that is created directly to the file
    # the with open syntax automatically closes file at end of block
    with open(text, 'w') as myfile:
    # use myfile as variable for iteration
        # iterate over each line in text creating it in newline for file
        for lines in text:
            myfile.write('\n'.join(str(lines) for line in lines))
            myfile.write('\n')
    # text argument will be the list of things created by user such as SSN name
    # When I call storecontent, I need to put the name of the list as the argument
