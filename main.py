# coding=utf-8
import json
import tarfile
import base64

def load_dot_vex(file_location):
    dot_vex_file = tarfile.open(file_location)
    dot_vex_file.extractall(".\\temp")
    dot_vex_file.close()
    with open(".\\temp\\___ThIsisATemPoRaRyFiLE___.json") as content:
        dot_vex_json: dict = json.load(content)
        print(dot_vex_json["files"])
        for x in dot_vex_json["files"]:
            with open(x,"wb") as file:
                file.write(base64.b64decode(dot_vex_json["files"][x]))




def main():
    load_dot_vex(input("file location?"))
    print("test end")


if __name__ == '__main__':
        main()
