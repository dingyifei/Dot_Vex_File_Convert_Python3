# coding=utf-8
"""
I have nothing to say, it is a very simple program works
"""
import json
import tarfile
import base64
import os



def extract_dot_vex(vex_file_location: str, save_folder_location: str,temp_location, progress):
    """

    :param vex_file_location: the .vex file location, should include the .vex file
    :param save_folder_location:  the save folder location
    :param progress:  optional way to output the progress
    """

    progress("extracting json from .vex tar file")
    dot_vex_file = tarfile.open(vex_file_location)
    dot_vex_file.extractall(temp_location)
    dot_vex_file.close()
    progress("file extracted, loading json")
    with open(temp_location + "/___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        if not os.path.isdir(save_folder_location):
            os.mkdir(save_folder_location)
        progress("extracting and decode files from json")
        for x in dot_vex_json["files"]:
            with open(save_folder_location + "/" + x, "wb") as file:
                file.write(base64.b64decode(dot_vex_json["files"][x]))
        progress(str(len(dot_vex_json["files"])) + "Files extracted from .vex")


def update_dot_vex(vex_file_location: str,
                   save_folder_location: str,
                   save_file_name: str,
                   vex_decode_folder_location: str,
                   temp_location,
                   progress=print
                   ):
    """

    :param vex_file_location:  the old .vex file location, should include the .vex file
    :param save_folder_location: the folder to save .vex file
    :param save_file_name: the name of .vex file. should include .vex
    :param vex_decode_folder_location: the files you want to put into the .vex
    :param progress: optional way to output the progress
    """

    progress("extracting json from .vex tar file")
    dot_vex_file = tarfile.open(vex_file_location)
    dot_vex_file.extractall(temp_location)
    dot_vex_file.close()
    if not os.path.isdir(save_folder_location):
        os.mkdir(save_folder_location)
    progress("loading json")
    with open(temp_location + "/___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        encode_files: list = os.listdir(vex_decode_folder_location)
        progress("replacing file inside json")
        for x in encode_files:
            with open(vex_decode_folder_location + x, "rb") as file:
                dot_vex_json["files"][x] = base64.b64encode(file.read()).decode("utf-8")
    progress("replace the json file")
    os.remove(temp_location + "/___ThIsisATemPoRaRyFiLE___.json")
    with open(temp_location + "/___ThIsisATemPoRaRyFiLE___.json", "w") as content:
        json.dump(dot_vex_json, content)
    try:
        os.remove(save_folder_location + "/" + save_file_name)
    except:
        progress("we don't need to remove the json file")
    dot_vex_save_file = tarfile.open(save_folder_location + "/" + save_file_name, "w")
    dot_vex_save_file.add(
        temp_location +
        "/___ThIsisATemPoRaRyFiLE___.json",
        "/___ThIsisATemPoRaRyFiLE___.json")

    dot_vex_save_file.close()
    progress("replace/update .vex file complete")


def main():
    """
    I have no idea why someone try to run this and say it is not working....
    """

    print(
        "You are running it in the console, it have less feature than the converter_ui \n try converter_ui.py")

    mode = input("do you want to extract a .vex file (choose 1), or update a .vex file (Choose 2)?")
    if mode == 1:
        vex_file = input("vex file location?")
        save_dir = input("where do you want save the files?")
        extract_dot_vex(vex_file, save_dir, print)

    elif mode == 2:
        vex_file = input("vex file location?")
        save_dir = input("where do you want save the files?")
        save_name = input("save name?")
        open_dir = input("What do you want to save into the vex file?")
        update_dot_vex(vex_file, save_dir, save_name, open_dir)

    else:
        print("handle weird input is just annoying")


if __name__ == '__main__':
    main()
