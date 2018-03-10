from app_backend import api, db
from flask_restful import Resource
from flask import jsonify, request
from models.user import User
import datetime


class UserAPI(Resource):
    """
    Handles the queries to create and modify user entry

    Requirements
    ------------
    Les utilisateurs peuvent renseigner/modifier leurs informations
    personnelles sur la plateforme (nom, prénom, date de naissance)
    """

    def post(self):
        """
        Creation of a user entry

        Returns
        -------

        _ : JSON
            Validation of creation

        """
        # All the fields are mandatory here
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        # Format the birth date to Date
        birth_date_str = request.json.get('birth_date')
        birth_date_list = birth_date_str.split('-')
        birth_date = datetime.date(int(birth_date_list[0]),
                                   int(birth_date_list[1]),
                                   int(birth_date_list[2]))

        user_ = User(first_name, last_name, birth_date)
        # Insert the new user in the table
        db.session.add(user_)
        db.session.commit()

        return jsonify({'status': 200,
                        'method': 'HTTP POST',
                        'uri': '/userapi',
                        'user_id': user_.id,
                        'first_name': user_.first_name,
                        'last_name': user_.last_name,
                        'birth_date': str(user_.birth_date)
                        })

    def put(self):
        """
        Modification of a user entry provided the ID of the user in the
        request

        Returns
        -------

        _ : JSON
            Validation of modification

        """
        id_ = request.json.get('id')
        # Retrieve the user
        user_ = User.query.get(id_)
        if user_ is None:
            return jsonify({'status': 403,
                            'method': 'HTTP PUT',
                            'uri': '/userapi',
                            'user_uuid': id_,
                            'message': 'Invalid user uuid'
                            })

        for key in request.json.keys():
            if key == 'first_name':
                first_name = request.json.get('first_name')
                user_.first_name = first_name
            if key == 'last_name':
                last_name = request.json.get('last_name')
                user_.last_name = last_name
            if key == 'birth_date':
                # Format the birth date to Date
                birth_date_str = request.json.get('birth_date')
                birth_date_list = birth_date_str.split('-')
                birth_date = datetime.date(int(birth_date_list[0]),
                                           int(birth_date_list[1]),
                                           int(birth_date_list[2]))
                user_.birth_date = birth_date

        # Commit the modification
        db.session.commit()

        return jsonify({'status': 200,
                        'method': 'HTTP PUT',
                        'uri': '/userapi',
                        'user_id': user_.id,
                        'first_name': user_.first_name,
                        'last_name': user_.last_name,
                        'birth_date': str(user_.birth_date)
                        })


api.add_resource(UserAPI, '/userapi', endpoint='userapi')
