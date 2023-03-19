# JSON - JavaScript Object Notation
# Load, change and save functions

import json


def openJson():
    try:
        with open("files/test.json", encoding="UTF-8") as test_file:
            data = json.load(test_file)
            changeConfig(data)
    except FileNotFoundError:
        print("err: open - file not found")
    except json.decoder.JSONDecodeError:
        print("err: open - json decode")


def changeConfig(data):
    data["test1"]["value"] = "Bonjour le monde"
    saveJson(data)


def saveJson(file):
    try:
        with open("files/out_test.json", "w", encoding="UTF-8") as out_file:
            json.dump(file, out_file, ensure_ascii=False)
            print("ok: file saved")
    except FileNotFoundError:
        print("err: save - file not found")


openJson()
