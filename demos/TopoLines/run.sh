#!/bin/bash

# delete old directories
if [ "$1" = "clean" ]
then
    rm -rf __pycache__
    rm -rf lcsmooth/__pycache__
    rm -rf topology/__pycache__
    rm -rf rdp/__pycache__
    rm -rf venv
    rm -rf entropy
    rm tmp_*.pd
    rm -rf hera
fi

if [ ! -d "venv/" ]; then

  # Create Virtual Environment
  python3 -m venv venv

  # Activate the environment
  . venv/bin/activate

  pip install --upgrade pip

  # Within the activated environment, use the following command to install Flask and dependancies:
  pip install wheel numpy sklearn simplejson Flask python-dotenv watchdog blinker gunicorn matplotlib colorutils

  # Install Entropy library
  git clone https://github.com/raphaelvallat/entropy.git entropy/
  cd entropy/
  pip install -r requirements.txt
  python setup.py develop
  cd ..

  deactivate

  # Clone hera
  git clone https://bitbucket.org/grey_narn/hera.git
  git checkout d72ebd3ede77c887e0f4fbb3d9c1410fb38f23ba

  # Patching for macport error
  patch hera/bottleneck/CMakeLists.txt hera_macport.patch

  # Build Hera Bottleneck
  mkdir hera/bottleneck/bin
  cd hera/bottleneck/bin
  cmake ..
  make
  cd ../../../

  # Build Hera Wasserstein
  mkdir hera/wasserstein/bin
  cd hera/wasserstein/bin
  cmake ..
  make
  cd ../../../

fi


# Activate the environment
. venv/bin/activate

export HERA_BOTTLENECK="hera/bottleneck/bin/bottleneck_dist"
export HERA_WASSERSTEIN="hera/wasserstein/bin/wasserstein_dist"

python server.py

deactivate


