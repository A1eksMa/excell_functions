#!/bin/bash

# Create list of categories
list=("compatibility" "cube" "database" "datetime" "engineering" "financial" "information" "lookup" "math" "statistical" "text" "users" "web")

# Make folders
for folder in "${list[@]}"
do
    rm -r "$folder"
done
