# The idea is to store multiple thing on your clipboard.
# Three different commands save, load and list.
# To store what we've copied, we're gonna map what is currently
# on the clipboard with a key.

import sys
import clipboard
import json

# The idea is to store all clipboard items in a json file

# paste() - get the data from the user's clipboard
#data = clipboard.paste()

# copy() - to store the data on the clipboard
# clipboard.copy("Me la chupas mamaguevo")

SAVED_DATA = "clipboard.json"

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)

def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# json - JavaScript Object Notation :)

# Using the python command arguments
if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ") 
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else: 
            print("Key doesn't exits")
    elif command == "list":
        print(data)
    else: 
        print("Unknown command")
else:
    print("Please pass exactly one command")