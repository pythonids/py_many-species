# YAML - Yet Another Markup Language
# Load, change and save functions

# https://pyyaml.org/wiki/PyYAMLDocumentation
# pip install pyyaml
import yaml


def openYaml(n):
    open("files/out_test.yaml", "w")

    # test.yaml - k8s sample configuration
    with open(r'files/test.yaml') as test_file:
        # yaml.FullLoader - conversion from YAML to dictionary
        i = 0
        for data in yaml.load_all(test_file, Loader=yaml.FullLoader):
            changeConfig(data)
            saveYaml(data, i, n)
            i += 1


def changeConfig(data):
    data['apiVersion'] = "newVersion1"


def saveYaml(file, i, n):
    with open(r'files/out_test.yaml', 'a') as out_file:
        if i < n:
            yaml.dump(file, out_file)
            if i < n - 1:
                out_file.write("---\n")


# openYaml(number_of_documents)
openYaml(3)
