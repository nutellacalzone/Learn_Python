#The line below imports argv module from sys
from sys import argv
#The line below sets script and filename to argv
script, filename = argv
#The line below sets a variable named txt equal to an open file you specify
txt = open(filename)
#The lines below this prints the specified file from above to the screen via the 'read' command
print "Here's your file %r:" % filename
print txt.read()
#The line below prints out a statement to the console prompting the user to type their specified filename again. They could also type a different filename that happens to be located in the same directory.
print "Type the filename again:"
file_again = filename
#The line below sets the variable text_again equal to the specified file to open
txt_again = open(file_again)
#The line below this prints the file's read contents to the screen.
print txt_again.read()
