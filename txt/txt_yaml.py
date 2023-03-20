# YAML - Yet Another Markup Language
# Load, change and save functions

# https://pyyaml.org/wiki/PyYAMLDocumentation
# pip install pyyaml

# python txt_json.py

import yaml


def openYaml(n):
    open("files/out.yaml", "w")

    # test.yaml - k8s sample configuration
    try:
        with open(r'files/in.yaml') as test_file:
            # yaml.FullLoader - conversion from YAML to dictionary
            i = 0
            for data in yaml.load_all(test_file, Loader=yaml.FullLoader):
                changeConfig(data)
                saveYaml(data, i, n)
                i += 1
    except FileNotFoundError:
        print("err: open - file not found")
    except TypeError:
        print("err: open - yaml decode")


def changeConfig(data):
    data['apiVersion'] = "newVersion1"
    return data


def saveYaml(file, i, n):
    try:
        with open(r'files/out.yaml', 'a') as out_file:
            if i < n:
                yaml.dump(file, out_file)
                print("ok: file saved")
                if i < n - 1:
                    out_file.write("---\n")
    except FileNotFoundError:
        print("err: save - file not found")


# openYaml(number_of_documents)
openYaml(3)
