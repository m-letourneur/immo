import requests

if __name__ == '__main__':
    """
    Initialization of the database.

    Creation of user instances and estate instances
    """
    headers = {
        'Content-Type': "application/json",
    }

    # Users
    url = "http://127.0.0.1:5000/userapi"
    # User 1
    payload = "{\n\"first_name\":\"Jean\",\n\"last_name\":\"Bernard\",\n\"birth_date\":\"1959-01-12\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    user1_id = response.json()['user_id']

    # User 2
    payload = "{\n\"first_name\":\"Alexe\",\n\"last_name\":\"Dupond\",\n\"birth_date\":\"1963-04-01\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    user2_id = response.json()['user_id']

    # User 3
    payload = "{\n\"first_name\":\"Michel\",\n\"last_name\":\"Sanchez\",\n\"birth_date\":\"1989-10-21\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    user3_id = response.json()['user_id']

    # Estates
    url = "http://127.0.0.1:5000/estateapi"
    # Estate 1
    payload = "{\n\"creator_uuid\": \"" + \
        str(user1_id) + "\",\n\"city\": \"Paris\",\n\"nb_rooms\": 2,\n\"description\": \"Nice 2-room flat located in city center next to Gardens\",\n\"rooms_description\": \"1 bedroom, one kitchen\",\n\"owner\": \"Jean Philippe\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)

    # Estate 2
    payload = "{\n\"creator_uuid\": \"" + \
        str(user2_id) + "\",\n\"city\": \"Caen\",\n\"nb_rooms\": 10,\n\"description\": \"Old farm house\",\n\"rooms_description\": \"5 bedrooms\",\n\"owner\": \"J-D D\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # Estate 3
    payload = "{\n\"creator_uuid\": \"" + \
        str(user2_id) + "\",\n\"city\": \"Caen\",\n\"nb_rooms\": 3,\n\"description\": \"Flat next to the river\",\n\"rooms_description\": \"2 bedrooms\",\n\"owner\": \"X Dupond\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)

    # Estate 4
    payload = "{\n\"creator_uuid\": \"" + \
        str(user2_id) + "\",\n\"city\": \"Granville\",\n\"nb_rooms\": 3,\n\"description\": \"Flat, Harbour view, great opportunity\",\n\"rooms_description\": \"2 bedrooms\",\n\"owner\": \"Jean Daniel\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)

    # Estate 5
    payload = "{\n\"creator_uuid\": \"" + \
        str(user3_id) + "\",\n\"city\": \"Paris\",\n\"nb_rooms\": 1,\n\"description\": \"Renovated studio\",\n\"rooms_description\": \"Integrated kitchenette\",\n\"owner\": \"Marcel P\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)

    print("\nThe database has been initialized with few instances.\n")
