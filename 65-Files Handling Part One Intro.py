#-----------------------
#-- File Handling ------
#-----------------------
#"a" => append Open File For Appending Values, create File If Not Exists
# "r" => Read [Default Valuse] Open File For Read and Give Error If Not Exists
#"w" => Write Open File For Writing, Create File If Not Exists
#"x" => Create Create File, Give Error If File Exists
#-------------------------------------------------------------------

import os

# Main Current Working Directory
#print(os.getcwd())

# Diectory For The Opened File
#print(os.path.dirname(os.path.abspath(__file__)))

#Change Current Working Directory
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

#print(os.path.abspath(__file__))

file = open(r"C:\\Users\\APPLE\\Desktop\\Python\\file.txt", "w") # Create File If Not Exists



