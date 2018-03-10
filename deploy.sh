#!/bin/bash
#Here are the commands to run in a terminal

cd "/Users/Marc/Downloads"

# Clone the repository
git clone "https://mletourneur3@bitbucket.org/mletourneur3/immo.git"
cd immo 
git checkout dev

# Create a virtual environment to work on
source `which virtualenvwrapper.sh`
mkvirtualenv --python=`which python3.6` immo2
source $WORKON_HOME/immo2/bin/activate immo2
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
# Initialize db handler in API
python3.6 api.py db init
python3.6 api.py db migrate
python3.6 api.py db upgrade 

# Run the API
python3.6 api.py runserver