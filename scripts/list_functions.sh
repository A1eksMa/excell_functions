#!/var/www/html/data-analysts/venv/bin/python3
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
    open("./__init__.py",  "a").write("# " + 
                                      df['Function'][i] + 
				      "\ndef " + 
				      df['Function'][i][0:-9] + 
				      "():\n    ''" + 
				      df['Description'][i] + 
				      "''" + 
				      "\n    pass\n    return\n\n\n")
