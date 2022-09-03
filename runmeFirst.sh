#!/bin/bash 


echo "Hello World!"
echo "$PWD"
python -c 'print("hey Python")'
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

