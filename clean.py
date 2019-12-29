import os
import shutil
import datetime

### If Recycle_Bin folder doesn't exist on my Desktop, create it ###
#if not os.path.exists('C:\\users\\ischlesinger\\Desktop\\Recycle_Bin\\'):
    #os.makedirs('C:\\users\\ischlesinger\\Desktop\\Recycle_Bin\\')
    


### Creating variables date / time and for moving files on my desktop ###
now = str(datetime.datetime.now())[:19]
now = now.replace(":","_")
source = 'C:\\users\\ischlesinger\\Desktop\\'
dest1 = 'C:\\users\\ischlesinger\\Desktop\\Recycle_Bin\\'
files = os.listdir(source)

### If file is not "Recycle_Bin" nor "clean.py", add today's date / time and move from Desktop to Recycle_Bin ###
for f in files:
    if f != "Recycle_Bin" and f != "clean.py" and f != "vim_cheat_sheet.txt":
        if not os.path.exists(dest1+f):
            shutil.move(source+f, dest1)
        else:
            rename = source+str("("+now+") ")+f
            shutil.move(source+f, rename)
            shutil.move(rename, dest1)

   

### Move clean.py file from "Recycle_Bin" to my desktop ###   
#if not os.path.exists('C:\\users\\ischlesinger\\Desktop\\clean.py'):
    #shutil.move('C:\\users\\ischlesinger\\Desktop\\Recycle_Bin\\clean.py', #'C:\\users\\ischlesinger\\Desktop\\clean.py')
