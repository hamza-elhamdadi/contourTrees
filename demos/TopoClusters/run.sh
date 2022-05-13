#!/bin/bash

# delete old directories
if [ "$1" = "clean" ]
then
  # delete old directories
  rm -rf __pycache__
  rm -rf venv
fi

if [ ! -d "venv/" ]; then

  # Create Virtual Environment
  python3 -m venv venv

  # Activate the environment
  . venv/bin/activate

  pip install --upgrade pip

  #Within the activated environment, use the following command to install Flask and dependancies:
  pip install wheel sklearn numpy flask matplotlib
  
else

  # Activate the environment
  . venv/bin/activate

fi

python server.py

deactivate
