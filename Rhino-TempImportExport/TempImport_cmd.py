import rhinoscriptsyntax as rs

__commandname__ = "TempImport"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    import rhinoscriptsyntax as rs
    import tempfile
    import os
    
    rs.DocumentModified(False)
    file = tempfile.gettempdir() + os.sep + "TempImportExport.dxf"
    file_handle = open(file, 'r')
    cmd = "_Import " + chr(34) + file + chr(34)
    rs.Command(cmd, True)