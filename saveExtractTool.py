import sys, os, pathlib
import os.path
import xml.etree.ElementTree as ET

try:
    import pyctr
    from pyctr.crypto import CryptoEngine, Keyslot
    from pyctr.type.ncch import NCCHReader
    from pyctr.type.tmd import TitleMetadataReader
    
except ImportError:
    print("Error pyctr version 0.1.0 is required")
    exit()

def main():
    print(len(sys.argv))
    if len(sys.argv) < 9:
        print("""Arguments missing. Required arguments are:
Nintendo 3DS folder
--inputFolder folderPath
Movable.sed path:
--movable movablePath
Output folder:
--outputFolder folderPath
Path to disa-extract.py:
--disa disaPath
""")
        return None

    inputFolder = None
    outputFolder = None
    movablePath = None
    disaPath = None
    
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
        elif sys.argv[i] == "--disa" or sys.argv[i] ==  "-e":
            i += 1
            disaPath = sys.argv[i]
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
    if disaPath is None:
        print("Path to disa-extract.py is not present")
    
    if inputFolder is None or outputFolder is None or movablePath is None or disaPath is None :
        return None

    print("All paths parsed")
    if not(pathlib.Path(inputFolder).is_dir()):
        print("Input folder directory does not exist. Inputted path: {}".format(inputFolder))
    if not(pathlib.Path(outputFolder).is_dir()):
        print("Output folder directory does not exist. Inputted path: {}".format(outputFolder))
    if not(os.path.isfile(movablePath)):
        print("movable does not exist. Inputted path: {}".format(movablePath))
    if not(os.path.isfile(disaPath)):
        print("disa_extract.py does not exist. Inputted path: {}".format(disaPath))

    print("Creating crypto object, if this creates an error then boot9.bin is not found")
    crypto = CryptoEngine()

    print("Setting movable.sed for decryption")
    crypto.setup_sd_key_from_file(movablePath)

    print("Getting directories in Nintendo 3DS")
    #id0 = selectDirectory32char(inputFolder)
    id0 = crypto.id0
    id0 = id0.hex()
    
    print("Getting directories in {}".format(id0))
    id1 = selectDirectory32char(inputFolder + "\\" + id0)
    
    print("Starting dump and decrypt.")

    for titleHigh in os.listdir(inputFolder + "\\" + id0 + "\\" + id1 + "\\title\\"):
        print("Title High: {}".format(titleHigh))
        for titleLow in os.listdir(inputFolder + "\\" + id0 + "\\" + id1 + "\\title\\" + titleHigh + "\\"):
            print("Title Low: {}".format(titleLow))
            appFile = selectAppFile(crypto, inputFolder + "\\" + id0 + "\\" + id1 + "\\title\\" + titleHigh + "\\" + titleLow + "\\" + "content" + "\\")
            return None

def selectAppFile(crypto, inputPath):
    files = os.listdir(inputPath)

    tmdFile = None
    
    for i in range(len(files)):
        if ".tmd" in files[i] and tmdFile == None:
            tmdFile = files[i]

    path = inputPath + tmdFile

    split_path = path.split("\\")
    sd_path = "/" + split_path[len(split_path)-5]
    for i in range(len(split_path)-4, len(split_path)):
        sd_path += "/" + split_path[i]
    
    print(path)
    print(sd_path)
    with open(path) as fh:
        with crypto.create_ctr_io(Keyslot.SD, fh, crypto.sd_path_to_iv(sd_path)) as sd_file:
            tmd = TitleMetadataReader.load(sd_file)
            first_record = tmd.chunk_records[0]
            first_record_id = first_record.id

    print(first_record_id)
    return None
def selectDirectory32char(inputPath):
    directories = os.listdir(inputPath)
    
    for i in range(len(directories)):
        if len(directories[i]) != 32:
            directories.pop(i)
            
    if len(directories) == 1:
        directory = directories[0]
    elif len(directories) == 0:
        print("No folders in {}".format(inputPath))
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
    return directory

if __name__ == "__main__":
    main()
