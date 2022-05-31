import rhinoscriptsyntax as rs
import tempfile
import os

def TempImport():
    rs.DocumentModified(False)
    file = tempfile.gettempdir() + os.sep + "TempImportExport.dwg"
    file_handle = open(file, 'r')
    cmd = "_Import " + chr(34) + file + chr(34)
    rs.Command(cmd, True)

if __name__=="__main__":
    TempImport()