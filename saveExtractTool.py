import sys

def main():
    if len(sys.argv < 8):
        print("""Arguments missing. Required arguments are:
Nintendo 3DS folder
--inputFolder folderPath
Free drive letter:
--drive driveLetter
Movable.sed path:
--movable movablePath
Output folder:
--outputFolder folderPath
""")
        break
    
