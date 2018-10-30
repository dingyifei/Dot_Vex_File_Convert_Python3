# coding=utf-8

import dot_vex_convert
import os
from tkinter import *
from tkinter.filedialog import *


def main():
    root = Tk()
    root.title(".vex Converter")
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # variables (Changeable)
    code_folder = StringVar()
    temp_folder = StringVar()
    vex_open = StringVar()
    vex_save_folder = StringVar()
    vex_save_name = StringVar()

    # Column 1
    status_label = Label(mainframe, text="Status: ")
    status_label.grid(column=1, row=1, sticky=(W, N))

    code_folder_label = Label(mainframe, text="Code Folder: ")
    code_folder_label.grid(column=1, row=2, sticky=(W, N))

    temp_folder_label = Label(mainframe, text="Temp Folder: ")
    temp_folder_label.grid(column=1, row=3, sticky=(W, N))

    vex_open_label = Label(mainframe, text=".vex Open: ")
    vex_open_label.grid(column=1, row=4, sticky=(W, N))

    vex_save_folder_label = Label(mainframe, text=".vex Save Folder: ")
    vex_save_folder_label.grid(column=1, row=5, sticky=(W, N))

    vex_save_name_label = Label(mainframe, text=".vex Save Name: ")
    vex_save_name_label.grid(column=1, row=6, sticky=(W, N))

    def extract_decode():
        progress_show_label["text"] = "extracting"
        dot_vex_convert.extract_dot_vex(vex_open.get(), code_folder.get())
        progress_show_label["text"] = "extract complete"

    extract_decode_button = Button(mainframe, text="Extract and Decode", command=extract_decode)
    extract_decode_button.grid(column=1, row=7, sticky=(N, W))

    progress_text_label = Label(mainframe, text="Progress: ")
    progress_text_label.grid(column=1, row=8, sticky=(W, N))

    # Column 2

    status_show_label = Label(mainframe, text="Nothing here yet")
    status_show_label.grid(column=2, row=1, sticky=(N, W))

    code_folder_entry = Entry(mainframe, width=15, textvariable=code_folder)
    code_folder_entry.grid(column=2, row=2, sticky=(N, W))

    temp_folder_entry = Entry(mainframe, width=15, textvariable=temp_folder)
    temp_folder_entry.grid(column=2, row=3, sticky=(N, W))

    vex_open_entry = Entry(mainframe, width=15, textvariable=vex_open)
    vex_open_entry.grid(column=2, row=4, sticky=(N, W))

    vex_save_folder_entry = Entry(mainframe, width=15, textvariable=vex_save_folder)
    vex_save_folder_entry.grid(column=2, row=5, sticky=(N, W))

    vex_save_name_entry = Entry(mainframe, width=15, textvariable=vex_save_name)
    vex_save_name_entry.grid(column=2, row=6, sticky=(N, W))

    def convert_to_dot_vex():
        progress_show_label["text"] = "converting"
        dot_vex_convert.update_dot_vex(vex_open.get(), vex_save_folder.get(), vex_save_name.get(), code_folder.get())
        progress_show_label["text"] = "convert complete"

    convert_vex_button = Button(mainframe, text="Convert to .vex File", command=convert_to_dot_vex)
    convert_vex_button.grid(column=2, row=7, sticky=(N, E))

    progress_show_label = Label(mainframe, text="")
    progress_show_label.grid(column=2, row=8, sticky=(W, N))

    # Column 3

    def get_help():
        help_window = Tk()
        help_window.title("Help")
        help_frame = Frame(help_window)
        help_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        help_frame.columnconfigure(0, weight=1)
        help_frame.rowconfigure(0, weight=1)
        help_label = Label(help_frame, text="this is the test text for helping window \n this is the test text")
        help_label.grid(column=1, row=1, sticky=(N, E, W, S))
        help_frame.mainloop()

    help_button = Button(mainframe, text="Help", command=get_help)
    help_button.grid(column=3, row=1, sticky=(N, E))

    def code_folder_ask():
        code_folder.set(askdirectory())

    code_folder_button = Button(mainframe, text="Browse", command=code_folder_ask)
    code_folder_button.grid(column=3, row=2, sticky=(N, E))

    def temp_folder_ask():
        temp_folder.set(askdirectory())

    temp_folder_button = Button(mainframe, text="Browse", command=temp_folder_ask)
    temp_folder_button.grid(column=3, row=3, sticky=(N, E))

    def vex_open_ask():
        vex_open.set(askopenfilename(filetypes=[("Vex files", "*.vex")]))

    vex_open_button = Button(mainframe, text="Browse", command=vex_open_ask)
    vex_open_button.grid(column=3, row=4, sticky=(N, E))

    def vex_save_folder_ask():
        vex_save_folder.set(askdirectory())

    vex_save_folder_button = Button(mainframe, text="Browse", command=vex_save_folder_ask)
    vex_save_folder_button.grid(column=3, row=5, sticky=(N, E))

    # Start the window
    root.mainloop()


def browse_button():
    # filename = askdirectory()
    print("This is reserved")
    return "This is reserved"


if __name__ == '__main__':
    main()
