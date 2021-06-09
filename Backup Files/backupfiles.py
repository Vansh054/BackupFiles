import os
import shutil
import time
import datetime

os.system('cls')

path = 'C:/Users/pc/Downloads'
folderTime = ""
actualTime = time.time()

print(actualTime, "actual")

if (os.path.exists(path)):
    folderName = os.listdir(path)
    for a in folderName:
        currentPath = os.path.join(path, a)
        ##print(currentPath)
        root, ext = os.path.splitext(currentPath)
        ctime = os.stat(currentPath).st_ctime
        # print(ctime)
        folderTime = actualTime - ctime
        existence = actualTime - folderTime
        # print(existence)

        """ datetime_time = datetime.datetime.fromtimestamp(existence)

        print(datetime_time) """
        if existence < 1615275279:
            if ext != '' : 
                    os.remove(currentPath)


else:
    print("Path doesn't exits")

# 1623225111.2756999
