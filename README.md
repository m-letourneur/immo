# README

## Introduction

Please, find here my answer to the case.

We considered 2 types of data:

- users, that create and update estate entries
- estates, created by users, that can be modified and queried with respect to the attribute `city`


We did not implement authentication for users.
We assume that the platform, hosting the services, is handling the requests for the users. Thus, the platform handles encryption of the requests. But, this being said, we could implement encryption for at least the admin of the platform. This has not been implemented.

### Future work
Other features that have not been implemented and that may be necessary
	
- Better handle customized exceptions through API
- Check input format, especially for dates
- API authentication layer
- Duplicate checking in database at instantiation and modification
- Other methods for endpoints: deletion of entries, get listing per user...
- Incorporate other tests


## Data model

The model is a SQL scheme.

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
* 	city TEXT: city location
* 	nb_rooms INT: number of rooms
* 	description TEXT: description of the estate
* 	rooms_description TEXT: description of rooms
* 	owner TEXT: owner of the estate

3 fields are mandatory:	

	uuid (primary key)
	creator_uuid
	city
	nb_rooms

## Endpoints

### Host name
HOSTNAME will refer to the running host.
It might be by default http://127.0.0.1:5000/ on your machine.
It can also refer to a host in the cloud. 

### User - Create
POST a new user

#### Resource URL

http://HOSTNAME/userapi

#### Resource Information

Response formats          | Requires authentication?      
------------- | ------------- 
JSON  | No 

#### Parameters
Name          | Required      | Description   | Value               | Example 
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
first\_name  | yes   | first name   | string | "Jean"
last\_name  | yes   | last name   | string | "Melin"
birth\_date  | yes   | date of birth, format "yyyy-mm-dd"  | string | "1989-02-03"

#### Request example

```
curl -X POST \
  http://HOSTNAME/userapi \
  -H 'Content-Type: application/json' \
  -d '{
"first_name":"Jean-Claude",
"last_name":"Dilo",
"birth_date":"1959-01-12"
}'
```

#### Response example

	{
	    "birth_date": "1959-01-12",
	    "first_name": "jean-claude",
	    "last_name": "dilo",
	    "method": "HTTP POST",
	    "status": 200,
	    "uri": "/userapi",
	    "user_id": "6a6cd0f4bbe444578d7426e478ba5e88"
	}

### User - Modify an existing user entry
PUT user information

#### Resource URL

http://HOSTNAME/userapi

#### Resource Information

Response formats          | Requires authentication?      
------------- | ------------- 
JSON  | No 

#### Parameters
Name          | Required      | Description   | Value               | Example 
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
id  | yes   | uuid of the user  | integer | 6a6cd0f4bbe444578d7426e478ba5e88
first\_name  | no   | first name   | string | "Jean"
last\_name  |  no  | last name   | string | "Melin"
birth\_date  | no   | date of birth, format "yyyy-mm-dd"  | string | "1989-02-03"

#### Request example

```
curl -X PUT \
  http://HOSTNAME/userapi \
  -H 'Content-Type: application/json' \
  -d '{
"id" : "6a6cd0f4bbe444578d7426e478ba5e88",
"birth_date":"1929-01-12"
}'
```


#### Response example

	{
	    "birth_date": "1929-01-12",
	    "first_name": "Jean-Claude",
	    "last_name": "Dilo",
	    "method": "HTTP PUT",
	    "status": 200,
	    "uri": "/userapi",
	    "user_id": "6a6cd0f4bbe444578d7426e478ba5e88"
	}
	
### Estate - Create
POST a new estate

#### Resource URL

http://HOSTNAME/estateapi

#### Resource Information

Response formats          | Requires authentication?      
------------- | ------------- 
JSON  | No 

#### Parameters
Name          | Required      | Description   | Value               | Example 
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
creator_uuid  | yes   | uuid of the user creating the instance   | integer | 6a6cd0f4bbe444578d7426e478ba5e88
city  | yes   | city location   | string | "Caen"
nb_rooms  | yes   |  number of rooms  | integer | 2
description  | no   | description of the property   | string | "Nice 2-room flat located in city center next to Gardens"
rooms_description  | no   | description of the rooms   | string | "1 bedroom, one kitchen"
owner  | no   | Name of the owner | string | "Jean Philippe Dublin"

#### Request example
	curl -X POST \
	  http://HOSTNAME/estateapi \
	  -H 'Content-Type: application/json' \
	  -d '{
		"creator_uuid": "6a6cd0f4bbe444578d7426e478ba5e88",
		"city": "Melbourne",
		"nb_rooms": 2,
		"description": "Nice 2-room flat located in city center next to Gardens",
		"rooms_description": "1 bedroom, one kitchen",
		"owner": "Jean Philippe"
	}'
	
#### Response example
	{
	    "city": "melbourne",
	    "creator_uuid": "6a6cd0f4bbe444578d7426e478ba5e88",
	    "description": "nice 2-room flat located in city center next to gardens",
	    "estate_id": "02828e559ba645ac8b84e6fb833e7050",
	    "method": "HTTP POST",
	    "nb_rooms": 2,
	    "owner": "jean philippe",
	    "rooms_description": "1 bedroom, one kitchen",
	    "status": 200,
	    "uri": "/estateapi"
	}
	
### Estate - Modify entry
PUT estate information if and only if the UUID of the user matches the UUID of the creator of the estate instance

#### Resource URL

http://HOSTNAME/estateapi

#### Resource Information

Response formats          | Requires authentication?      
------------- | ------------- 
JSON  | No 

#### Parameters
Name          | Required      | Description   | Value               | Example 
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
id  | yes   | uuid of the estate instance to modify | integer | 02828e559ba645ac8b84e6fb833e7050
creator_uuid  | yes   | uuid of the user creating the instance   | integer | 6a6cd0f4bbe444578d7426e478ba5e88
city  | no   | city location   | string | "Caen"
nb_rooms  | no   |  number of rooms  | integer | 2
description  | no   | description of the property   | string | "Nice 2-room flat located in city center next to Gardens"
rooms_description  | no   | description of the rooms   | string | "1 bedroom, one kitchen"
owner  | no   | Name of the owner | string | "Jean Philippe Dublin"

#### Request example
	curl -X PUT \
	  http://HOSTNAME/estateapi \
	  -H 'Content-Type: application/json' \
	  -d '{
	"id": "02828e559ba645ac8b84e6fb833e7050",
	"creator_uuid": "6a6cd0f4bbe444578d7426e478ba5e88",
	"rooms_description": "No toilet in the bedroom"
	}'
	
#### Response example
	{
	    "city": "Caen",
	    "creator_uuid": "6a6cd0f4bbe444578d7426e478ba5e88",
	    "description": "Nice 2-room flat located in city center next to Gardens",
	    "estate_id": "02828e559ba645ac8b84e6fb833e7050",
	    "method": "HTTP POST",
	    "nb_rooms": 2,
	    "owner": "Jean Philippe Dublin",
	    "rooms_description": "No toilet in the bedroom",
	    "status": 200,
	    "uri": "/estateapi"
	}

### Estate - Get listing per city
GET the list of estate instances matching the city in input

#### Resource URL

http://HOSTNAME/estateapi/<string:city>

#### Resource Information

Response formats          | Requires authentication?      
------------- | ------------- 
JSON  | No 

#### Parameters
Name          | Required      | Description   | Value               | Example 
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
city  | no   | city location   | string | "Caen"

#### Request example

	curl -X GET http://HOSTNAME/estateapi/caen

#### Response example

	{
	    "city": "caen",
	    "list of estates in city": "[<Estate uuid = 7418be6e13b443cfb5f53faae03ecb1d, creator_uuid = 9fb52a3b7bf243baae900dfe034eaea0, description = caen, city = old farm house, nb_rooms = 10, rooms_description = 5 bedrooms, owner = j-d d>, <Estate uuid = e443e6d23d18474ea45d5af32412d045, creator_uuid = 9fb52a3b7bf243baae900dfe034eaea0, description = caen, city = flat next to the river, nb_rooms = 3, rooms_description = 2 bedrooms, owner = x dupond>]",
	    "method": "HTTP GET",
	    "status": 200,
	    "uri": "/estateapi"
	}

## Install and run the API on local host


### Method 1 - manual setup
Here are the commands to run in a terminal
> cd /path/to/dir/

#### Clone the repository
> git clone [https://mletourneur3@bitbucket.org/mletourneur3/immo.git]()
>
> cd immo 

#### Create a virtual environment to work on
> mkvirtualenv --python=`which python3.6` immo
>
> pip install -r requirements.txt

#### Initialize the database
> cd database/

> sqlite3

##### With SQLITE3
> .read immodb.sqlite
> 
> .quit

##### Back to console - use the manager
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

### METHOD 2 - script
If you have cloned the repository already, you can use the deploy.sh script.
Adjust the path to directory (line 4) and run in console:
> cd /path/to/immo/
> 
> bash deploy.sh

#### Initialize the database
> python3.6 database/db_init.py

## Tests

Tests written in tests/test_local.py to run basic functions of the local API
> python3.6 test/test_local.py

To test the cloud version
> python3.6 test/test_cloud.py


## Cloud services

We deployed the API in the cloud using one AWS EC2 instance and Docker.
The docker file is in the cloud/ directory.

	HOSTNAME = 52.221.231.209:8000

Example

	curl -X GET http://52.221.231.209:8000/estateapi/caen
