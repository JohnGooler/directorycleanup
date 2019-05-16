"""
Use OS for get the directory and manage it for delete not important dir an clean up

"""
import os
import sys
import shutil

GIVEN_DIR = sys.argv[1]
LIST_OF_DIRECTORY = os.listdir(GIVEN_DIR)
MY_DIR = os.path.dirname(os.path.realpath(__file__))


with open(MY_DIR + "\\exc.txt") as f:
    NEVER_DELETE_DIR = f.readlines()
    NEVER_DELETE_DIR = [x.strip() for x in NEVER_DELETE_DIR]


for i in LIST_OF_DIRECTORY:
    if i in NEVER_DELETE_DIR:
        pass
    else:
        if os.path.isfile(os.path.join(GIVEN_DIR, i)):
            os.remove(os.path.join(GIVEN_DIR, i))
        elif os.path.isdir(os.path.join(GIVEN_DIR, i)):
            shutil.rmtree(os.path.join(GIVEN_DIR, i), ignore_errors=True)
