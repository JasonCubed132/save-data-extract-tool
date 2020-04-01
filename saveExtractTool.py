import sys, os, pathlib

def main():
    if len(sys.argv < 14):
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
        break

    inputFolder = None
    outputFolder = None
    moveablePath = None
    driveLetter = None
    ninfsPath = None
    disaPath = None
    releasesPath = None
    
    i = 1
    while i < len(sys.argv[i]):
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
            
    if inputFolder is None:
        print("Input folder is not present")
    if outputFolder is None:
        print("Output folder is not present")
    if moveablePath is None:
        print("Movable path is not present")
    if driveLetter is None:
        print("Drive letter is not present")
    if ninfsPath is None:
        print("Path to ninfs is not present")
    if disaPath is None:
        print("Path to disa-extract.py is not present")
        
    if inputFolder is None or outputFolder is None or moveablePath is None or driveLetter is None or ninfsPath is None or disaPath is None:
        break

    if !pathlib.Path(inputFolder).is_dir():
        print("Input folder directory does not exist. Inputted path: {}".format(inputFolder))
    if !pathlib.Path(outputFolder).is_dir():
        print("Output folder directory does not exist. Inputted path: {}".format(outputFolder))
    if !os.path.isFile(moveablePath):
        print("Moveable does not exist. Inputted path: {}".format(moveablePath))
    if !os.path.isFile(ninfsPath):
        print("ninfs.exe does not exist. Inputted path: {}".format(ninfsPath))
    if !os.path.isFile(disaPath):
        print("disa_extract.py does not exist. Inputted path: {}".format(disaPath))
    
    
