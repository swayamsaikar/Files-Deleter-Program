import os
import shutil
import time

path = input("Enter A File Directory Path\n")
currentTimeInSeconds = time.time()


def deletefiles(path, currentTimeInSeconds):
    if not os.path.exists(path):
        print("Please Provide a valid path")
    if os.path.isfile(path):
        print("Please Provide a Directory Path")
    else:
        files = os.listdir(path)
        for each_file in files:
            f = os.path.splitext(each_file)
            # f[1] means the second element in this tuple ('file1', '.txt')

            if(f[1] == ""):
                # This Code is For Folders
                folderPath = os.path.join(path, each_file)

                calculationForFolder = currentTimeInSeconds - os.stat(
                    folderPath).st_ctime

                if calculationForFolder > currentTimeInSeconds:
                    shutil.rmtree(folderPath)
                    print("Folder Deleted Successfully")

                # print(calculationForFolder)
                # print(currentTimeInSeconds)

            if (not f[1] == ""):
                # This Code Is For Files
                filePath = os.path.join(path, each_file)
                CalculationForFile = currentTimeInSeconds - \
                    os.stat(filePath).st_ctime

                if CalculationForFile > currentTimeInSeconds:
                    shutil.remove(folderPath)
                    print("File Deleted Successfully")

                # print(CalculationForFile)
                # print(currentTimeInSeconds)


deletefiles(path, currentTimeInSeconds)

# MAM I HAVE NOT TESTED IT
