import requests

hostname = "http://127.0.0.1:5000"
user_id_for_test = None
estate_id_for_test = None
headers = {
    'Content-Type': "application/json",
}


def test_ping():
    """
    Basic ping pong test
    """
    url =  hostname + "/ping"
    response = requests.request("GET", url)
    assert response.json()['status'] == 200
    print("Test - Ping - SUCCESS")


def test_create_user():
    """
    Creates a user with valid inputs
    """
    global headers, user_id_for_test
    headers = {
        'Content-Type': "application/json",
    }
    url = hostname + "/userapi"

    payload = "{\n\"first_name\":\"Jean\",\n\"last_name\":\"Bertrand\",\n\"birth_date\":\"1959-12-12\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    user_id_for_test = response.json()['user_id']
    assert user_id_for_test is not None
    print("Test - Create user - SUCCESS")


def test_modify_user():
    """
    Modify user info with valid inputs 
    """
    global headers, user_id_for_test
    headers = {
        'Content-Type': "application/json",
    }
    url = hostname + "/userapi"

    payload = "{\n\"id\" : \"" + user_id_for_test + \
        "\",\n\"birth_date\":\"2000-12-12\"\n}"
    response = requests.request("PUT", url, data=payload, headers=headers)
    assert response.json()['status'] == 200
    birth_date = response.json()['birth_date']
    assert birth_date == '2000-12-12'
    print("Test - Modify user - SUCCESS")


def test_modify_user_invalid_uuid():
    """
    Modify user info with invalid uuid 
    """
    global headers, user_id_for_test
    url = hostname + "/userapi"

    payload = "{\n\"id\" : \"" + \
        str(0) + "\",\n\"birth_date\":\"2000-12-12\"\n}"
    response = requests.request("PUT", url, data=payload, headers=headers)
    assert response.json()['status'] == 403
    print("Test - Modify user with invalid uuid - SUCCESS")


def test_create_estate():
    """
    Create estate with valid inputs 
    """
    global headers, user_id_for_test, estate_id_for_test
    url = hostname + "/estateapi"

    payload = "{\n\"creator_uuid\": \"" + \
        str(user_id_for_test) + "\",\n\"city\": \"Paris\",\n\"nb_rooms\": 2,\n\"description\": \"Nice 2-room flat located in city center next to Gardens\",\n\"rooms_description\": \"1 bedroom, one kitchen\",\n\"owner\": \"Jean Philippe\"\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    assert response.json()['status'] == 200
    estate_id_for_test = response.json()['estate_id']
    print("Test - Create estate - SUCCESS")


def test_modify_estate():
    """
    Create estate with valid user uuid
    """
    global headers, user_id_for_test, estate_id_for_test
    url = hostname + "/estateapi"

    payload = "{\n\"id\": \"" + \
        str(estate_id_for_test) + "\",\n\"creator_uuid\": \"" + \
        str(user_id_for_test) + \
        "\",\n\"rooms_description\": \"No toilet in the bedroom\"\n}"
    response = requests.request("PUT", url, data=payload, headers=headers)
    assert response.json()['status'] == 200
    print("Test - Modify estate with valid creator uuid - SUCCESS")


def test_modify_estate_invalid_user():
    """
    Create estate with invalid user uuid
    """
    global headers, user_id_for_test, estate_id_for_test
    url = hostname + "/estateapi"

    payload = "{\n\"id\": \"" + \
        str(estate_id_for_test) + "\",\n\"creator_uuid\": \"" + \
        str(0) + "\",\n\"rooms_description\": \"No toilet in the bedroom\"\n}"
    response = requests.request("PUT", url, data=payload, headers=headers)
    assert response.json()['status'] == 403
    print("Test - Modify estate with invalid creator uuid - SUCCESS")


def test_modify_estate_invalid_estate_uuid():
    """
    Create estate with invalid estate uuid
    """
    global headers, user_id_for_test, estate_id_for_test
    url = hostname + "/estateapi"

    payload = "{\n\"id\": \"" + \
        str(0) + "\",\n\"creator_uuid\": \"" + \
        str(user_id_for_test) + \
        "\",\n\"rooms_description\": \"No toilet in the bedroom\"\n}"
    response = requests.request("PUT", url, data=payload, headers=headers)
    assert response.json()['status'] == 403
    print("Test - Modify estate with invalid estate uuid - SUCCESS")


def test_listing_per_city():
    """
    Get listing
    """
    global headers, user_id_for_test, estate_id_for_test
    url = hostname + "/estateapi/Paris"

    response = requests.request("GET", url)
    assert response.json()['status'] == 200
    print("Test - Get listing per city - SUCCESS")


if __name__ == '__main__':
    test_ping()
    test_create_user()
    test_modify_user()
    test_modify_user_invalid_uuid()
    test_create_estate()
    test_modify_estate()
    test_modify_estate_invalid_user()
    test_modify_estate_invalid_estate_uuid()
    test_listing_per_city()
