import os
print("*** This application creates files using the same name and appends numbers for each sequential file. Example: 'test1.txt, test2.txt, et cetera ***")

def makefiles(count):
    number = 0
    filename = input("Enter filename for testing: ")
    if not os.path.exists(dest1):
        os.makedirs(dest1)
    os.chdir(dest1)
    for i in range(count):
        number += 1
        f = open (filename + str(number) + ".txt", "w")
        f.close()

dest1 = 'C:\\users\\ischlesinger\\Desktop\\f_copy_Folder'        
total = int(input("Enter number of file: "))

makefiles(total)
