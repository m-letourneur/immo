#!/bin/bash
#Here are the commands to run in a terminal

# Add the path of your directory
cd "/Users/Marc/Downloads"

# Clone the repository
git clone "https://mletourneur3@bitbucket.org/mletourneur3/immo.git"
cd immo 

# Create a virtual environment to work on
source `which virtualenvwrapper.sh`
mkvirtualenv --python=`which python3.6` immo
source $WORKON_HOME/immo/bin/activate immo
# Install python packages
pip install -r "requirements.txt"

# Initialize the database with the manager
cd database/

# With sqlite3 create database
sqlite3 <<EOS
.read immodb.sqlite
.quit
EOS

# Back to console
cd ..
# Initialize db in API with manager
python3.6 api.py db init
python3.6 api.py db migrate
python3.6 api.py db upgrade 

# Run the API
python3.6 api.py runserver