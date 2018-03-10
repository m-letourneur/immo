# README

## Data model

### User
- uuid INT: unique ID for the user
- first_name TEXT: first name
- last_name TEXT: last name
- birth_date DATE: Date of birth, default format yyyy-mm-dd

All the fields are mandatory for the creation of a user.

	uuid is the primary key
	
### Estate
* 	uuid INT: unique ID for the estate entry
* 	creator_uuid INT: unique ID of the user who created the estate entry
* 	city TEXT NOT NULL: city location
* 	nb_rooms INT: number of rooms
* 	description TEXT: description of the estate
* 	rooms_description TEXT: description of rooms
* 	owner TEXT: owner of the estate

3 fields are mandatory:	

	uuid (primary key)
	creator_uuid
	city
	nb_rooms

## Services

TO WRITE

## Install and run the API on Local host
### METHOD 1 - script
Run in console:
> bash deploy.sh

### Method 2 - manual setup
Here are the commands to run in a terminal
> cd 
>
> mkdir immo

#### Clone the repository
> git clone [git]()
>
> cd immo 

#### Create a virtual environment to work on
> mkvirtualenv --python=`which python3.6` immo
>
> pip install -r requirements.txt

#### Initialize the database with the manager
> cd database/

> sqlite3
##### With SQLITE3
> .read immodb.sqlite
> .quit

##### Back to console
> cd ..

> python3.6 api.py db init
> 
> python3.6 api.py db migrate
> 
> python3.6 api.py db upgrade
> 

#### Run the API
> python3.6 api.py runserver

#### Initialize the database
> python.3.6 database/db_init.py

#### Try services

TO WRITE

## To do

- Create a script to initilize the db
- Finish resources userapi and estates and test
- Add exceptions for duplicates, ...(?)