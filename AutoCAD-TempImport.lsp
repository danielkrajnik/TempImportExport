(defun c:TempImport ()
  (command "insert" (strcat (getenv "TEMP") "\\TempImportExport.dxf") "0,0,0" "1" "1" "0")
  (command "explode" "last")
  (command "purge" "b" "TempImportExport" "n")
  (princ)
)