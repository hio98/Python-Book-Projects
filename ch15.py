
#importing required modules from sys package
from sys import argv
#taking the argument apart and giving it to various parts
script, filename = argv
#open is used to open a file similar to fstream in C plus
txt = open(filename)
# a simple print function
print("Here's your file %r:" %filename)
#read function prints out the content of the text
print(txt.read())
#another simple print function
print("Type the filename again:")
#a prompt to input the filename again
file_again = input(">")
#read the new file
txt_again = open(file_again)
#another print statement
print(txt_again.read())
