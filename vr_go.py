#!/usr/bin/env python

import os

HOME_DIR = os.path.expanduser("~")
VIRTUAL_ENVIRONMENTS = "{0}/virtualenvs".format(HOME_DIR)

selection = -1
index = 0
directory_list = []
for directory in os.listdir(VIRTUAL_ENVIRONMENTS):
    if not directory.startswith("."):
        index += 1
        print "{0}. {1}".format(index, directory)
        directory_list.append(directory)

print "0. Exit"

while selection != 0:
    selection = int(raw_input(
        "Select an environment to activate."))

if selection == 0:
    print "No environment activated."
    exit()
else:
    SELECTED_VIRTUAL_ENVIRONMENT = "{0}/{1}".format(VIRTUAL_ENVIRONMENTS, directory_list[selection-1])
    ACTIVATION_CALL = ". {0}/bin/activate".format(SELECTED_VIRTUAL_ENVIRONMENT)

    activator = open("help_activate.sh", "w")
    activator.write("#!/bin/bash\n")
    activator.write("{0}\n".format(ACTIVATION_CALL))
    activator.close()

    os.system("/bin/bash --rcfile help_activate.sh")
    os.remove("help_activate.sh")
