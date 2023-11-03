#!/bin/bash

# Create list of categories
list=("compatibility" "cube" "database" "datetime" "engineering" "financial" "information" "logical" "lookup" "math" "statistical" "text" "users" "web")

# Make folders
for folder in "${list[@]}"
do
    cd ..
#    mkdir "$folder"
    cd "$folder"
#    str="# "
#    str+="$folder"
#    echo "$str" >>__init__.py

#    cp "../scripts/list_functions.sh" ./
#    cp "../scripts/$folder.csv" ./
    # Run script, writing code from template in __init__.py file
    # sudo "./list_functions.sh"
    # Clear
    rm "./list_functions.sh"
    # rm "./$folder.csv"
done
