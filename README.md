# Toolbars for Windows 11

Toolbars was removed in windows 10. This is a python implementation of toolbars using tkinter.

![Example](https://github.com/SoulsCalibre/Win11Toolbars/blob/main/example.gif)


## Requirements

This script requires Python 3 to be installed on the system along with the following packages:

-   `win32com`
-   `tkinter`
-   `pyinstaller`

## Installation

To use the script, first clone the repository from GitHub:

`git clone https://github.com/SoulsCalibre/Win11Toolbars.git`

Next, navigate to the cloned repository and install the required packages using pip:

```
cd Win11Toolbars
pip install -r requirements.txt
```

Run `build_list_widget.bat` to compile `list_widget.pyw` into an exe file. You should see a folder named `list_widget` in the directory.

## Usage

To use the script, run the following command in the terminal:

`python create_shortcut.py [name] [folder]`

`name`: The name of the toolbar. If not provided, the script will prompt for it.

`folder`: The path of the folder to be added to the toolbar. If not provided, the script will prompt to select a folder using a GUI window.

Alternatively, you can run the script without arguments and a prompt to type the name and select a folder will be available.

This script will create shortcuts in the toolbar folder. You can pin these shortcuts to the taskbar and change their icons.

## Why compile `list_widget.pyw` into an exe file?

Python files are not able to be pinned to the taskbar. Exe files and shortcuts to them can.

## Notes

The first time `list_widget.exe` is run, windows defender might block it and scan the file instead. Let it scan the file and this should only happen on the first run.

This program will show the extension of the file if there are multiple files in the directory of the same name.
