:: Create Virtual Environment
python3 -m venv venv

:: Activate the environment
venv\Scripts\activate.bat

:: Within the activated environment, use the following command to install Flask and dependancies:
pip install wheel
pip install numpy sklearn simplejson Flask python-dotenv watchdog blinker gunicorn matplotlib colorutils

# Install Entropy library
powershell -command "Expand-Archive -Force entropy.zip entropy"

cd entropy/
pip install -r requirements.txt
python setup.py develop
cd ..
