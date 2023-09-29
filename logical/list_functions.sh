#!/usr/bin/python3
# encoding: utf-8
import pandas as pd
import os
# Get folder name
cwd = os.getcwd()
os.chdir("../")
bwd = os.getcwd()
curdir = cwd.replace(bwd + "/", "")
os.chdir("./" + curdir)

category = curdir
df = pd.read_csv(category + ".csv", sep=";")

for i in range(len(df)):
    open("./" + category + ".py",  "a").write("# " + df['Function'][i] + " function\n# " + df['Description'][i] + "\n\ndef " + df['Function'][i] + "():\n    try:\n        pass\n        return\n    except:\n        return\n\n")
