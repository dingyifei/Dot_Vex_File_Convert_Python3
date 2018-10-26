# coding=utf-8
import json
import tarfile


def load_dot_vex(file_location):
    dot_vex_file = tarfile.open(file_location)
    dot_vex_file.extractall(".\\temp")
    dot_vex_file.close()
    with open(".\\temp\\___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        print((list(dot_vex_json.keys())))


def main():
    load_dot_vex("C:\\users\\13676\\Desktop\\V5_Robot_2\\Competition_control.vex")
    print("test end")


if __name__ == '__main__':
        main()
