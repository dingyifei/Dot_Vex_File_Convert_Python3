# coding=utf-8
'''
I have nothing to say, it is a very simple program that works properly
'''
import json
import tarfile
import base64
import os

DEFAULT_TEMP_FILE_LOCATION = ".\\temp\\"


def load_dot_vex(vex_file_location: str, save_folder_location: str):
    """

    :param vex_file_location: the .vex file location, should include the .vex file
    :param save_folder_location:  the save folder location
    """
    dot_vex_file = tarfile.open(vex_file_location)
    dot_vex_file.extractall(DEFAULT_TEMP_FILE_LOCATION)
    dot_vex_file.close()
    with open(FAULT_TEMP_FILE_LOCATION + "___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        print(dot_vex_json["files"])
        for x in dot_vex_json["files"]:
            with open(save_folder_location + x, "wb") as file:
                file.write(base64.b64decode(dot_vex_json["files"][x]))


def update_dot_vex(
        vex_file_location: str, save_folder_location: str, save_file_name: str, vex_decode_folder_location: str):
    """

    :param vex_file_location:  the old .vex file location, should include the .vex file
    :param save_folder_location: the folder to save .vex file
    :param save_file_name: the name of .vex file. should include .vex
    :param vex_decode_folder_location: the files you want to put into the .vex
    """
    dot_vex_file = tarfile.open(vex_file_location)
    dot_vex_file.extractall(DEFAULT_TEMP_FILE_LOCATION)
    dot_vex_file.close()
    with open(DEFAULT_TEMP_FILE_LOCATION + "___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        encode_files: list = os.listdir(vex_decode_folder_location)
        for x in encode_files:
            with open(vex_decode_folder_location + x, "rb") as file:
                y = file.read()
                y = base64.b64encode(y).decode("utf-8")
                print(y)
                dot_vex_json["files"][x] = y
    os.remove(DEFAULT_TEMP_FILE_LOCATION + "___ThIsisATemPoRaRyFiLE___.json")
    with open(DEFAULT_TEMP_FILE_LOCATION + "___ThIsisATemPoRaRyFiLE___.json", "w") as content:
        json.dump(dot_vex_json, content)

    os.remove(save_folder_location + save_file_name)
    dot_vex_save_file = tarfile.open(save_folder_location + save_file_name, "w")
    dot_vex_save_file.add(DEFAULT_TEMP_FILE_LOCATION + "___ThIsisATemPoRaRyFiLE___.json"
                          , "___ThIsisATemPoRaRyFiLE___.json")

    dot_vex_save_file.close()


def main():
    load_dot_vex(".\\V5_Robot_2\\Competition_control.vex", ".\\decoded\\")
    update_dot_vex(".\\V5_Robot_2\\Competition_control.vex", ".\\temp\\", "output.vex", ".\\decoded\\")
    print("test end")


if __name__ == '__main__':
        main()
