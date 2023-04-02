from os import scandir as os_scandir, startfile as os_startfile, path as os_path
from sys import argv as sys_argv, exit as sys_exit
import tkinter as tk
from win32gui import GetCursorPos
from win32api import GetMonitorInfo, MonitorFromPoint

def get_files(directory):
    '''Returns a dictionary of basename:fullpath pair in a directory'''
    files = {}
    for file in os_scandir(directory):
        name, ext = os_path.splitext(os_path.basename(file))
        if name in files:
            files[name].append(ext)
        else:
            files[name] = [ext]
    return files


class FileListWidget(tk.Frame):
    def __init__(self, directory):
        self.loaded = False  # Do not close program until it is loaded

        self.root = tk.Tk()
        self.directory = directory
        self.root.overrideredirect(True)
        self.root.geometry("+250+250")  # set initial position of the window
        self.root.config(bg="#282C34")  # dark background color
        self.root.attributes("-topmost", True)  # always on top

        self.listbox = tk.Listbox(self.root, bg="#282C34", fg="white",
                                  selectbackground="#3E4452", highlightthickness=0,
                                  font=("Segoe UI", 11), bd=0, width=20)  # customizations
        self.listbox.pack(fill='both', expand=True)
        self.listbox.bind('<Button-1>', self.open_file)

        self.filenames = []  # lists would have faster access times than a dictionary here

        for file, ext in get_files(directory).items():
            if len(ext) == 1:
                self.listbox.insert('end', file)
                self.filenames.append(directory + '\\' + file + ext[0])
            else:
                for i in ext:
                    self.listbox.insert('end', file+i)
                    self.filenames.append(directory + '\\' + file + i)

        # Selection functions
        self.listbox.bind('<Enter>', self.on_enter)
        self.listbox.bind('<Motion>', self.on_motion)
        self.current_index = -1  # current item under mouse pointer

        # Resize the window to fit the listbox 
        self.root.geometry(f'{self.listbox.winfo_reqwidth()}x{self.listbox.winfo_reqheight()}')

        # Get the position of the mouse cursor
        cursor_x = GetCursorPos()[0]

        # Position the tkinter window right above the taskbar icon
        # Get the height of the taskbar
        monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
        taskbar_height = monitor_info.get("Monitor")[3] - monitor_info.get("Work")[3]

        x = cursor_x - (self.root.winfo_reqwidth() // 2)
        y = self.root.winfo_screenheight() - self.listbox.winfo_reqheight() - taskbar_height
        self.root.geometry(f"+{x}+{y}")

        self.listbox.focus_set()  # give focus to the listbox widget

        # make the window act as if you right clicked a regular windows icon in the taskbar
        self.root.bind('<Escape>', self.close_window)
        self.root.bind('<FocusOut>', self.close_on_lose_focus)

        # No title bar
        self.root.overrideredirect(1)

        # Allow the window to close after it is loaded
        def start_listen():
            self.loaded = True
        self.root.after(0, self.listbox.focus_set)
        self.root.after(1, start_listen)
        self.root.mainloop()

    # Functions
    def on_enter(self, event):
        """Highlight the file that the mouse is over when the mouse enters the listbox"""
        self.current_index = self.listbox.nearest(event.y)
        self.update_selection()

    def on_motion(self, event):
        """Highlight the file that the mouse is over when the mouse moves from one file to another"""
        index = self.listbox.nearest(event.y)
        if index != self.current_index:
            self.current_index = index
            self.update_selection()

    def update_selection(self):
        """Change the selection"""
        self.listbox.selection_clear(0, 'end')
        self.listbox.selection_set(self.current_index)
        self.listbox.activate(self.current_index)

    def open_file(self, event):
        """Open selected file and close the window"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            # filename = self.listbox.get(index)
            os_startfile(os_path.join(self.directory, self.filenames[index]))
            self.root.destroy()

    def close_window(self, event):
        """Close window"""
        self.root.destroy()

    def close_on_lose_focus(self, event=None):
        """Close window if user clicks out of it"""
        if self.root.focus_get() != self.root and self.loaded:
            self.root.destroy()
        self.root.after(10, self.close_on_lose_focus)

if __name__ == '__main__':
    if len(sys_argv) < 2:
        sys_exit()  # Using sys.exit() so script can be compiled into an exe.

    directory = sys_argv[1]
    file_list_widget = FileListWidget(directory)
