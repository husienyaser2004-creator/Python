#------------------------------------
#---Files Handling Part 2 Read Files-
#------------------------------------

import os

print(os.getcwd()) # Get Current Working Directory
print(os.listdir()) # Get Current Working Directory Files

my_file = open("hussien.txt", "r")

#print(my_file) # File Data Object 
#print(my_file.name) # File Name
#print(my_file.mode) # File Mode
#print(my_file.readable()) # File Readable

#print(my_file.read()) # Read All File Data
#print(my_file.read(5)) # Read All File Data

#print(my_file.readline(5)) # Read Line By Line
#print(my_file.readline()) # Read Line By Line
#print(my_file.readline()) # Read Line By Line

#print(my_file.readlines()) # Read All Lines In List
#print(my_file.readlines(50)) # Read All Lines In List
#print(my_file.readlines()) # Read All Lines In List

for line in my_file:

    print(line) # Read All Lines In List

my_file.close() # Close File