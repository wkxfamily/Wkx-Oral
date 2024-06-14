Set objShell = CreateObject("WScript.Shell")

Set objFSO = CreateObject("Scripting.FileSystemObject")
scriptdir = objFSO.GetParentFolderName(objFSO.GetFile(WScript.ScriptFullName))

bits = GetObject("winmgmts:root\cimv2:Win32_Processor='cpu0'").AddressWidth

if bits = 64 then
  objShell.Exec scriptdir & "\pbcdview.x64.exe"
else
  objShell.Exec scriptdir & "\pbcdview.exe"
end if
