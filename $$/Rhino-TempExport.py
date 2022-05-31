import rhinoscriptsyntax as rs
import tempfile
import os

def TempExport():
    rs.DocumentModified(False)
    
    file = tempfile.gettempdir() + os.sep + "TempImportExport.dwg"
    file_handle = open(file, 'w')
    cmd = "_Export " + chr(34) + file + chr(34)
    rs.Command(cmd, True)

if __name__=="__main__":
    TempExport()