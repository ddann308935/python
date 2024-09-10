# File Modes
    # "r" - read
    # "w" - write
    # "a" - append
    # "x" - exclusive creation

# Open and Close a file 

f = open("prgm/Week_7/shoppingList.txt")
f.close()
print("Is the file closed?", f.closed)

# alternatively (indent to automatically close the file)

with open("prgm/Week_7/shoppingList.txt") as f:
    print(f.read())

print("Is the file closed?", f.closed)

# Reading from a file
    # f.read()
    # f.readline()
    # f.readlines()

# Writing to a file
    # f.write()
    # f.writeline()

# Append a file
    # f.append()

# Get Current Directory

import os
curr_dir = os.getcwd()
print(curr_dir)

# Change Current Directory and Raw Strings

import os
os.chdir(r'newpath/newpath/newpath/newpath')
changed_dir = os.getcwd()
print(changed_dir)

# Make a New Directory 
# if the full path is not specified,
# the new directory is created in the
# current working directory

import os
print(os.getcwd())
os.mkdir('SecretMoney')
os.mkdir('BuriedTreasure')
os.mkdir('BitcoinWallet')
os.mkdir('Secrets')

# List of Subdirectories and files
# if no path is specified, it returns a list
# from the current working directory

import os
print(os.listdir('path/path/path'))

# Test if a directory exists
# returns a bool

import os
print(os.path.exists(r'C://path/path/path'))

# Removing a directory or file

import os
os.remove('path/path/file')
os.rmdir('path/path/path')

# Check the size of a directory
# returns the size in bytes

import os
os.path.getsize('path/path/path')

