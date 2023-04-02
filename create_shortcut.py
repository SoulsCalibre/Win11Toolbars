import os
import sys
import win32com.client
from tkinter import filedialog
import tkinter as tk

def terminal_prompt():
    name = input("Name your toolbar: ").strip()
    shortcut_path = os.getcwd() + '\\toolbars\\' + name + '.lnk'
    if os.path.exists(shortcut_path):
        inp = input(f'The shortcut `{name}` already exists. Do you want to replace this? [Y/n]: ')
        if inp.lower() != 'y':
            quit()
            
    root = tk.Tk()
    root.withdraw()

    print('Select folder:')
    folder = filedialog.askdirectory().replace('/', '\\')

    return name, folder

if __name__ == '__main__':
    directory = os.getcwd() + '\\toolbars'
    if not os.path.exists(directory):
        os.makedirs(directory)

    if len(sys.argv) < 3:
        name, folder = terminal_prompt()
    else:
        name, folder = sys.argv[1], sys.argv[2].replace('/', '\\')
        while not os.path.exists(folder):
            print('Folder path does not exist')
            quit()

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(directory + '\\' + name + '.lnk')

    shortcut.TargetPath = os.getcwd() + r'\list_widget\list_widget.exe'
    shortcut.Arguments = folder
    shortcut.Save()
