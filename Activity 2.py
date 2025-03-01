file=open("MichaelJordan.txt","x")
file.close()

import os
if os.path.exists("NewFile.txt"):
    print("File already exists")
else:
    print("File does not exist")

import os
os.remove("MichaelJordan.txt")
