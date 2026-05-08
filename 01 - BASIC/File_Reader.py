file = "/home/dell/requirements.txt"

##MINIMAL RUN
#file_pointer = open(file, "r")
#print(file_pointer.read())
#file_pointer.close()

import os
file = "/home/dell/requirements.txt"
if os.path.exists(file):
    with open(file) as file_contents:
        for lines in file_contents:
            print(lines)
