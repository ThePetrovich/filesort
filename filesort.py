import os
from os import listdir
from os.path import isfile, join, isdir
from os import path
import shutil
import time

print("Hello!\nWelcome to FileSort 2.0.\nPlease set up folder associations in the following format:\n .extension folder\subfolder\etc \nExample: \n .zip Archives\Zip\nIf you want to put your folders somwhere, add 'dir folder\subfolder\etc' to the list.\nWhen you are done, type 'sort' to start the sorting process.")
strIn = ""

i = 0
associations = dict()
exts = set()
folders = set()

while True:
    data = input()
    if data == "sort":
        break
    temp = data.split(' ')
    associations[temp[0]] = temp[1]
    time.sleep(0.01)

for key, value in associations.items():
    print('{} {}'.format(key, value))
    exts.add(key)
    folders.add(value)

folderlist = list(folders)
extlist = list(exts)

absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))
cdir = os.getcwd()
onlyfiles = [f for f in listdir(cdir) if isfile(join(cdir, f))]
onlydirs = [f for f in listdir(cdir) if isdir(join(cdir, f))]
extensions = []
        
print("\nFiles in directory:\n------------------------------------------------")
for i in range(len(onlyfiles)):
    filename, file_extension = os.path.splitext(cdir+"\\"+onlyfiles[i])
    extensions.append(file_extension.lower())
    print(onlyfiles[i])
print("------------------------------------------------\n")

print("Directories:\n------------------------------------------------")
for i in range(len(onlydirs)):
    print(onlydirs[i])
print("------------------------------------------------\n")

print("Sorting in progress...")

for i in range(len(folderlist)):
    if not os.path.exists(cdir+"\\"+folderlist[i]):
        os.mkdir(cdir+"\\"+folderlist[i])
        print("Directory ", folderlist[i],  " created ")
    else:    
        print("Directory ", folderlist[i],  " already exists")

if (associations.get("dir") != None):
    for i in range(len(onlydirs)):
        try:
            print("Moving folder",onlydirs[i],"to",cdir+"\\"+associations["dir"])
            shutil.move(cdir+"\\"+onlydirs[i],cdir+"\\"+associations["dir"]+"\\"+onlydirs[i])
        except IOError:
            print("Cannot move folder",onlydirs[i])

for i in range(len(onlyfiles)):
    try:
        print("Moving file",onlyfiles[i],"to",cdir+"\\"+associations[extensions[i]])
        shutil.move(cdir+"\\"+onlyfiles[i], cdir+"\\"+associations[extensions[i]]+"\\"+onlyfiles[i])
    except IOError:
        print("Cannot move file",onlyfiles[i])
    except KeyError:
        print("No association for file",onlyfiles[i]+", skipping")

print("\nCleaning...")
for i in range(len(folderlist)):
    if not os.listdir(cdir+"\\"+folderlist[i]):
        os.rmdir(cdir+"\\"+folderlist[i])

print("\nDone!")
time.sleep(5)
input('Press ENTER to exit')