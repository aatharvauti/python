# Write a Python program to read,write and parse JSON files
import json

def readjson(filename):
    f = open(filename)
    data = json.load(f)
    print(f"\n READING FILE: {filename}\n")
    for x in data["student_details"]:
        print(x)


def writejson(filename, dictionary):
    with open(filename, "w") as f:
        json.dump(dictionary, f)


def parsejson(filename):
    f = open(filename)
    data = json.load(f)
    print(f"\n\n PARSING FILE: {filename}, FIELD: 'Email'\n")
    for x in range(len(data["student_details"])):
        print(" Email: " + data["student_details"][x]["Email"])
    print("\n")


dictionary = {
    "Name": "Mihir Doshi",
    "Email": "mihir.doshi15911@sakec.ac.in",
    "Branch": "Cybersecurity",
    "Mobile": "998714059728357"
}

readjson('sample.json')
writejson('sample2.json', dictionary)
parsejson('sample.json')


