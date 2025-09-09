import os
import pythoncom
from win32com.shell import shell, shellcon

def create_shortcut(target_path, shortcut_path, icon_path=None):
    shell_link = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink
    )

    shell_link.SetPath(target_path)
    
    if icon_path:
        shell_link.SetIconLocation(icon_path, 0)

    # Save the shortcut
    persist_file = shell_link.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(shortcut_path, 0)
