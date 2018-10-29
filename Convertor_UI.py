# coding=utf-8

import dot_vex_convert
import os

from tkinter import *
from tkinter.filedialog import *


def browse_button():
    # filename = askdirectory()
    print("This is reserved")
    return "This is reserved"


def main():
    root = Tk()
    root.title("hello")
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # variables (Changeable)
    code_folder = str
    temp_folder = str
    dot_vex_file_open = str
    dot_vex_file_save_folder = str
    dot_vex_file_save_name = str
    status = "Nothing here yet"

    # Column 1
    status_label = Label(mainframe, text="Status: ")
    status_label.grid(column=1, row=1, sticky=(W, N))

    code_folder_label = Label(mainframe, text="Code Folder: ")
    code_folder_label.grid(column=1, row=2, sticky=(W, N))

    temp_folder_label = Label(mainframe, text="Temp Folder: ")
    temp_folder_label.grid(column=1, row=3, sticky=(W, N))

    dot_vex_file_open_label = Label(mainframe, text=".vex Open: ")
    dot_vex_file_open_label.grid(column=1, row=4, sticky=(W, N))

    dot_vex_file_save_folder_label = Label(mainframe, text=".vex Save Folder: ")
    dot_vex_file_save_folder_label.grid(column=1, row=5, sticky=(W, N))

    dot_vex_file_save_name_label = Label(mainframe, text=".vex Save Name: ")
    dot_vex_file_save_name_label.grid(column=1, row=6, sticky=(W, N))

    dot_vex_file_save_name_label = Label(mainframe, text=".vex Save Name: ")
    dot_vex_file_save_name_label.grid(column=1, row=6, sticky=(W, N))

    # Column 2

    status_show_label = Label(mainframe, text=status)
    status_show_label.grid(column=2, row=1, sticky=(N, W))

    code_folder_entry = Entry(mainframe, width=15, textvariable=code_folder)
    code_folder_entry.grid(column=2, row=2, sticky=(N, W))

    temp_folder_entry = Entry(mainframe, width=15, textvariable=temp_folder)
    temp_folder_entry.grid(column=2, row=3, sticky=(N, W))

    dot_vex_file_open_entry = Entry(mainframe, width=15, textvariable=dot_vex_file_open)
    dot_vex_file_open_entry.grid(column=2, row=4, sticky=(N, W))

    dot_vex_file_save_folder_entry = Entry(mainframe, width=15, textvariable=dot_vex_file_save_folder)
    dot_vex_file_save_folder_entry.grid(column=2, row=5, sticky=(N, W))

    dot_vex_file_save_name_entry = Entry(mainframe, width=15, textvariable=dot_vex_file_save_name)
    dot_vex_file_save_name_entry.grid(column=2, row=6, sticky=(N, W))

    # Column 3

    help_button = Button(mainframe, text="Help", command=browse_button)
    help_button.grid(column=3, row=1, sticky=(N, E))

    code_folder_button = Button(mainframe, text="Browse", command=browse_button)
    code_folder_button.grid(column=3, row=2, sticky=(N, E))

    temp_folder_button = Button(mainframe, text="Browse", command=browse_button)
    temp_folder_button.grid(column=3, row=3, sticky=(N, E))

    dot_vex_file_open_button = Button(mainframe, text="Browse", command=browse_button)
    dot_vex_file_open_button.grid(column=3, row=4, sticky=(N, E))

    dot_vex_file_save_name_button = Button(mainframe, text="Browse", command=browse_button)
    dot_vex_file_save_name_button.grid(column=3, row=5, sticky=(N, E))

    # Start the window
    root.mainloop()


if __name__ == '__main__':
    main()
