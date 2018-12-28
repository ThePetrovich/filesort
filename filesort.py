import os
from os import listdir
from os.path import isfile, join, isdir
from os import path
import shutil
import time

print("Hello!\nWelcome to FileSort 2.2.\nType 'load' to load existing configuration, 'noload' to configure the program manually or 'exit' to close the program.")

i = 0
associations = dict()
exts = set()
folders = set()
noload = False
while True:
    temp0 = input()
    if temp0 == "load":
        try:
            fo = open("extensions.cfg", "r")
            lines = fo.read().splitlines()
            for i in range(len(lines)):
                temp = lines[i].split(' ')
                associations[temp[0]] = temp[1]
            fo.close()
            print("Configuration loaded succesfully.")
        except IOError:
            print("Could not read 'extensions.cfg', please configure associations manually.")
            noload = True
            time.sleep(1)
            print("Please set up folder associations in the following format:\n .extension folder\subfolder\etc \nExample: \n .zip Archives\Zip\nIf you want to put your folders somwhere, add 'dir folder\subfolder\etc' to the list.\nWhen you are done, type 'sort' to start the sorting process.")
            break
        break
    if temp0 == "exit":
        exit()
    if temp0 == "noload":
        noload = True
        break
    
while noload:
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
        os.makedirs(cdir+"\\"+folderlist[i])
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
        if (associations.get("*") == None):
            print("No association for file",onlyfiles[i]+", skipping")
        else:
            try:
                print("Moving file",onlyfiles[i],"to",cdir+"\\"+associations["*"])
                shutil.move(cdir+"\\"+onlyfiles[i], cdir+"\\"+associations["*"]+"\\"+onlyfiles[i])
            except IOError:
                print("Cannot move file",onlyfiles[i])
            

print("\nCleaning...")
try:
    for i in range(len(folderlist)):
        if not os.listdir(cdir+"\\"+folderlist[i]):
            os.rmdir(cdir+"\\"+folderlist[i])
except FileNotFoundError:
    print("Error while cleaning empty folders, aborting...")

print("\nDone!")
time.sleep(5)
input('Press ENTER to exit')
