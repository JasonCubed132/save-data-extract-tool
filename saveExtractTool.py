import sys, os, pathlib
import os.path
import xml.etree.ElementTree as ET
f

def main():
    print(len(sys.argv))
    if len(sys.argv) < 15:
        print("""Arguments missing. Required arguments are:
Nintendo 3DS folder
--inputFolder folderPath
Free drive letter:
--drive driveLetter
Movable.sed path:
--movable movablePath
Output folder:
--outputFolder folderPath
Path to ninfs.exe:
--ninfs ninfsPath
Path to disa-extract.py:
--disa disaPath
Path to 3dsreleases.xml:
--releases 3dsReleasesPath
""")
        return None

    inputFolder = None
    outputFolder = None
    movablePath = None
    driveLetter = None
    ninfsPath = None
    disaPath = None
    releasesPath = None
    
    i = 1
    while i < len(sys.argv):
        print(i, sys.argv[i])
        if sys.argv[i] == "--inputFolder" or sys.argv[i] ==  "-i":
            i += 1
            inputFolder = sys.argv[i]
        elif sys.argv[i] == "--outputFolder" or sys.argv[i] ==  "-o":
            i += 1
            outputFolder = sys.argv[i]
        elif sys.argv[i] == "--movable" or sys.argv[i] ==  "-m":
            i += 1
            movablePath = sys.argv[i]
        elif sys.argv[i] == "--drive" or sys.argv[i] ==  "-d":
            i += 1
            driveLetter = sys.argv[i]
        elif sys.argv[i] == "--ninfs" or sys.argv[i] ==  "-n":
            i += 1
            ninfsPath = sys.argv[i]
        elif sys.argv[i] == "--disa" or sys.argv[i] ==  "-e":
            i += 1
            disaPath = sys.argv[i]
        elif sys.argv[i] == "--releases" or sys.argv[i] ==  "-r":
            i += 1
            releasesPath = sys.argv[i]
        else:
            print("Unable to parse {}".format(sys.argv[i]))
        i += 1
    if inputFolder is None:
        print("Input folder is not present")
    if outputFolder is None:
        print("Output folder is not present")
    if movablePath is None:
        print("Movable path is not present")
    if driveLetter is None:
        print("Drive letter is not present")
    if ninfsPath is None:
        print("Path to ninfs is not present")
    if disaPath is None:
        print("Path to disa-extract.py is not present")
    if releasesPath is None:
        print("Path to 3dsreleases.py is not present")
    
    if inputFolder is None or outputFolder is None or movablePath is None or driveLetter is None or ninfsPath is None or disaPath is None or releasesPath is None:
        return None

    print("All paths parsed")
    if not(pathlib.Path(inputFolder).is_dir()):
        print("Input folder directory does not exist. Inputted path: {}".format(inputFolder))
    if not(pathlib.Path(outputFolder).is_dir()):
        print("Output folder directory does not exist. Inputted path: {}".format(outputFolder))
    if not(os.path.isfile(movablePath)):
        print("movable does not exist. Inputted path: {}".format(movablePath))
    if not(os.path.isfile(ninfsPath)):
        print("ninfs.exe does not exist. Inputted path: {}".format(ninfsPath))
    if not(os.path.isfile(disaPath)):
        print("disa_extract.py does not exist. Inputted path: {}".format(disaPath))
    if not(os.path.isfile(releasesPath)):
        print("3dsreleases.xml does not exist. Inputted path: {}".format(releasesPath))

    print("Attempting to mount {} to {} using {} by using {}".format(inputFolder, driveLetter, movablePath, ninfsPath))
    command = "\"" + ninfsPath + "\" sd -f \"" + inputFolder + "\" " + driveLetter + ": --movable \"" + movablePath + "\" -r"
    print(command)
    stream = os.popen(command)
    output = stream.read()
    print(output)

    if not(pathlib.Path(driveLetter + ":").is_dir()):
        print("Failed to mount")
        return None

    directories = os.listdir(driveLetter + ":")

    if len(directories) == 1:
        directory == directories[0]
    elif len(directory) == 0:
        print("No folders in mounted directores.")
        return None
    else:
        directory = None
        while directory == None:
            for i in range(len(directories)):
                print("{}: {}".format(i, directories[i]))
            directoryNum = input("Please input the number of the folder you wish to use: ")
            try:
                directoryNum = int(directoryNum)
            except:
                print("Inputted value was not a number.")
            if directoryNum > len(directories) - 1 or directoryNum < 0:
                print("Inputted value is not valid.")
            else:
                directory = directories[directoryNum]
    
    print("Opening 3dsreleases.xml")
    try:
        3dsreleases = open(releasesPath, "r")
    except FileNotFoundError:
        print("File not found, this should have been detected earlier.")
    
    print("Starting dump and decrypt.")

    for titleHigh in os.listdir(driveLetter + ":\\" + directory + "\\title\\"):
        print("Title High: {}".format(titleHigh))
        for titleLow in os.listdir(driveLetter + ":\\" + directory + "\\title\\" + titleHigh + "\\"):
            print("Title Low: {}".format(titleLow))
            
if __name__ == "__main__":
    main()
