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
* 	description TEXT: description of the estate
* 	city TEXT NOT NULL: city location
* 	nb_rooms INT: number of rooms
* 	rooms_description TEXT: description of rooms
* 	owner TEXT: owner of the estate

3 fields are mandatory:	

	uuid (primary key)
	creator_uuid
	city
	nb_rooms
	
## Install and run the API on Local host

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
> python3.6 api.py db init
> 
> python3.6 api.py db migrate
> 
> python3.6 api.py db upgrade
> 

#### Run the API
> python3.6 api.py runserver



## To do

- Create a script to initilize the db
- Finish resources userapi and estates and test
- Add exceptions for duplicates, ...(?)