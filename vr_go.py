#!/usr/bin/env python

import os

HOME_DIR = os.path.expanduser("~")
VIRTUAL_ENVIRONMENTS = "{0}/virtualenvs".format(HOME_DIR)

selection = 0
index = 1
directory_dict = {}
for directory in os.listdir(VIRTUAL_ENVIRONMENTS):
    if not directory.startswith("."):
        directory_dict[index] = "{0}".format(directory)
        index += 1

for key in directory_dict:
    print "{0}. {1}".format(key, directory_dict[key])
print "{0}. Exit".format(key+1)

min_selection = min(directory_dict)
max_selection = max(directory_dict) + 1

while True:
    selection = int(raw_input(
        "Select an environment to activate: "))
    if min_selection <= selection <= max_selection:
        break

if selection == max_selection:
    print "No environment activated."
    exit()
else:
    SELECTED_VIRTUAL_ENVIRONMENT = "{0}/{1}".format(
        VIRTUAL_ENVIRONMENTS, directory_dict[selection])

    os.system("/bin/bash --rcfile {0}/bin/activate".format(
        SELECTED_VIRTUAL_ENVIRONMENT))
