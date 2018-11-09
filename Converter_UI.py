# coding=utf-8

import vex_convert
import time
import os
import configparser
import logging
import threading
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox


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
    replace = BooleanVar()
    progress = StringVar()
    safe = BooleanVar()

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
        if temp_folder.get() != "":
            vex_convert.temp_location = temp_folder.get()
        vex_convert.extract_vex(vex_open.get(), temp_folder.get(), progress.set)
        vex_convert.decode_json(code_folder.get(), temp_folder.get(), progress.set)

    extract_decode_button = Button(
        mainframe, text="Extract and Decode", command=extract_decode)
    extract_decode_button.grid(column=1, row=7, sticky=(N, W))

    convert_type_checkbox = Checkbutton(
        mainframe, text="Convert between Vex C++ \n and C++ Pro during encode")
    convert_type_checkbox.grid(column=1, row=8, sticky=(W, N))

    progress_text_label = Label(mainframe, text="Progress: ")
    progress_text_label.grid(column=1, row=9, sticky=(W, N))

    # Column 2
    status_show_label = Label(mainframe, text="Nothing here yet")
    status_show_label.grid(column=2, row=1, sticky=(N, W))

    code_folder_entry = Entry(mainframe, width=30, textvariable=code_folder)
    code_folder_entry.grid(column=2, row=2, sticky=(N, W))

    temp_folder_entry = Entry(mainframe, width=30, textvariable=temp_folder)
    temp_folder_entry.grid(column=2, row=3, sticky=(N, W))

    vex_open_entry = Entry(mainframe, width=30, textvariable=vex_open)
    vex_open_entry.grid(column=2, row=4, sticky=(N, W))

    vex_save_folder_entry = Entry(mainframe, width=30, textvariable=vex_save_folder)
    vex_save_folder_entry.grid(column=2, row=5, sticky=(N, W))

    vex_save_name_entry = Entry(mainframe, width=30, textvariable=vex_save_name)
    vex_save_name_entry.grid(column=2, row=6, sticky=(N, W))

    def convert_to_dot_vex():
        if temp_folder.get == "":
            temp_folder.set("./temp/")
        vex_convert.extract_vex(vex_open.get(), temp_folder.get(), progress.set)
        vex_convert.update_json(code_folder.get(), temp_folder.get(), progress.set)
        if safe.get() is True:
            try:
                current_folder = os.getcwd()
                os.chdir(vex_save_folder.get())
                if os.path.isfile(vex_save_name.get() + ".backup"):
                    os.remove(vex_save_name.get() + ".backup")
                os.rename(vex_save_name.get(), vex_save_name.get() + ".backup")
                os.chdir(current_folder)
            except:
                progress.set("Did not rename old file")
        vex_convert.pack_vex(vex_save_folder.get(), vex_save_name.get(), temp_folder.get(), progress.set)

    convert_vex_button = Button(mainframe, text="Convert to .vex File", command=convert_to_dot_vex)
    convert_vex_button.grid(column=2, row=7, sticky=(N, E))

    def replace_command():
        if replace.get() is True:
            head, tail = os.path.split(vex_open.get())
            vex_save_name.set(tail)
            vex_save_folder.set(head)
            vex_save_folder_button["state"] = "disabled"
            vex_save_folder_entry["state"] = "disabled"
            vex_save_name_entry["state"] = "disabled"
        if replace.get() is False:
            vex_save_folder_button["state"] = "normal"
            vex_save_folder_entry["state"] = "normal"
            vex_save_name_entry["state"] = "normal"

    replace_checkbox = Checkbutton(mainframe,
                                   text="replace old .vex file", command=replace_command, variable=replace)
    replace_checkbox.grid(column=2, row=8, sticky=(W, N))

    progress_show_label = Label(mainframe, textvariable=progress)
    progress_show_label.grid(column=2, row=9, sticky=(W, N))

    # Column 3

    def get_help():
        help_window = Tk()
        help_window.title("Help")
        help_frame = Frame(help_window)
        help_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        help_frame.columnconfigure(0, weight=1)
        help_frame.rowconfigure(0, weight=1)
        help_label = Label(
            help_frame,
            text="this is the test text for helping window \n this is the test text")
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
        if replace.get() is True:
            replace_command()
        else:
            head, tail = os.path.split(vex_open.get())
            vex_save_name.set(tail)

    vex_open_button = Button(mainframe, text="Browse", command=vex_open_ask)
    vex_open_button.grid(column=3, row=4, sticky=(N, E))

    def vex_save_folder_ask():
        vex_save_folder.set(askdirectory())

    vex_save_folder_button = Button(
        mainframe, text="Browse", command=vex_save_folder_ask)
    vex_save_folder_button.grid(column=3, row=5, sticky=(N, E))

    def safe_command():
        print("something is here")

    safe_checkbox = Checkbutton(mainframe, text="safe", command=safe_command, variable=safe)
    safe_checkbox.grid(column=3, row=8, sticky=W)

    # ----------------------------------------------------------------------------------------------------------
    # load or create config file
    config = configparser.ConfigParser()

    def load_config():
        if os.path.isfile("./vex_convert.ini"):
            config.read(filenames="./vex_convert.ini")
            try:
                code_folder.set(config["DEFAULT"]["code_folder"])
                temp_folder.set(config["DEFAULT"]["temp_folder"])
                vex_open.set(config["DEFAULT"]["vex_open"])
                vex_save_folder.set(config["DEFAULT"]["vex_save_folder"])
                vex_save_name.set(config["DEFAULT"]["vex_save_name"])
                replace.set(config["DEFAULT"]["replace"])
                safe.set(config["DEFAULT"]["safe"])
            except:
                create_config()
                load_config()
        else:
            create_config()

    def create_config():
        if os.path.isfile("./vex_convert.ini"):
            os.remove("./vex_convert.ini")
        config["DEFAULT"] = {
            "code_folder": "",
            "temp_folder": "./temp/",
            "vex_open": "",
            "vex_save_folder": "",
            "vex_save_name": "",
            "replace": "False",
            "safe": "True"
        }
        with open("./vex_convert.ini", "w") as configfile:
            config.write(configfile)

    def save_config():
        config["DEFAULT"] = {
            "code_folder": code_folder.get(),
            "temp_folder": temp_folder.get(),
            "vex_open": vex_open.get(),
            "vex_save_folder": vex_save_folder.get(),
            "vex_save_name": vex_save_name.get(),
            "replace": replace.get(),
            "safe": safe.get()
        }
        with open("./vex_convert.ini", "w") as configfile:
            config.write(configfile)

    # When close
    def window_close():
        save_config()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", window_close)

    #Status Check
    def status_check():
        while True:
            if code_folder.get() != "" and temp_folder.get() != "" and vex_open.get() != "" and vex_save_folder.get() != "" and vex_save_name.get() != "":
                status_show_label["text"] = "Ready"
            else:
               status_show_label["text"] = "something is not right"
            time.sleep(0.5)
    status_checker = threading.Thread(target=status_check)

    # Start the window

    load_config()
    if replace.get() is True:
        vex_save_folder_button["state"] = "disabled"
        vex_save_folder_entry["state"] = "disabled"
        vex_save_name_entry["state"] = "disabled"

    status_checker.start()
    root.mainloop()


if __name__ == '__main__':
    main()
