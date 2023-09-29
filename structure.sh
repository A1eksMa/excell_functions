#!/bin/bash

# Create list of categories
list=("compatibility" "cube" "database" "datetime" "engineering" "financial" "information" "logical" "lookup" "math" "statistical" "text" "users" "web")

# Make folders
for folder in "${list[@]}"
do
    mkdir "$folder"
    cd "$folder"
    str="import "
    str+="$folder"
    echo "$str" >>__init__.py
    touch "$folder"".py"
    cd ../
done
