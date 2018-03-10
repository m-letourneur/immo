from app_backend import api, db
from flask_restful import Resource
from flask import jsonify, request, Response
from models.estate import Estate
from models.user import User
from flask import abort


class EstateAPI(Resource):
    """
    Handles the queries to create and modify estate entries
    Implements POST and PUT

    Requirements
    ------------
    1 - Un utilisateur peut modifier les caractéristiques d’un bien (changer 
    le nom, ajouter une pièce, etc… )

    2 - Un propriétaire ne peut modifier que les caractéristiques de son bien 
    sans avoir accès à l’édition des autres biens.
    """

    def post(self):
        """
        Creation of an estate entry by any user

        Returns
        -------

        _ : JSON
            Validation of creation

        """
        # Mandatory fields
        creator_uuid = request.json.get('creator_uuid')
        # Check if the id of the user is valid
        user_ = User.query.get(creator_uuid)
        if user_ is None:
            return jsonify({'status': 403,
                        'method': 'HTTP POST',
                        'uri': '/estateapi',
                        'creator_uuid': creator_uuid,
                        'message': 'Invalid user uuid (creator_uuid)'
                        })

        city = request.json.get('city')
        nb_rooms = request.json.get('nb_rooms')

        # Other non-mandatory fields
        description = None
        rooms_description = None
        owner = None
        for key in request.json.keys():
            if key == 'description':
                description = request.json.get('description')
            if key == 'rooms_description':
                rooms_description = request.json.get('rooms_description')
            if key == 'owner':
                owner = request.json.get('owner')

        # Instanciation with the model template
        estate_ = Estate(creator_uuid, city, nb_rooms, description,
                         rooms_description, owner)
        # Insert the new user in the table
        db.session.add(estate_)
        db.session.commit()

        return jsonify({'status': 200,
                        'method': 'HTTP POST',
                        'uri': '/estateapi',
                        'estate_id': estate_.id,
                        'creator_uuid': estate_.creator_uuid,
                        'city': estate_.city,
                        'nb_rooms': estate_.nb_rooms,
                        'description': estate_.description,
                        'rooms_description': estate_.rooms_description,
                        'owner': estate_.owner
                        })

    def put(self):
        """
        Creation of an estate entry by only allowed for the user that has 
        created it

        Returns
        -------

        _ : JSON
            Validation of modification

        """
        # Mandatory fields
        id_ = request.json.get('id')
        creator_uuid = request.json.get('creator_uuid')

        # Retrieve the estate
        estate_ = Estate.query.get(id_)
        if estate_ is None:
            return jsonify({'status': 403,
                        'method': 'HTTP PUT',
                        'uri': '/estateapi',
                        'estate_uuid': id_,
                        'message': 'Invalid user estate_uuid)'
                        })
            
        # Check if current user is the creator of the entry
        authorized = estate_.creator_uuid == creator_uuid

        if authorized:
            # Update any attribute provided in the form
            for key in request.json.keys():
                if key == 'nb_rooms':
                    nb_rooms = request.json.get('nb_rooms')
                if key == 'city':
                    city = request.json.get('city')
                    estate_.city = city
                if key == 'description':
                    description = request.json.get('description')
                    estate_.description = description
                if key == 'rooms_description':
                    rooms_description = request.json.get('rooms_description')
                    estate_.rooms_description = rooms_description
                if key == 'owner':
                    owner = request.json.get('owner')
                    estate_.owner = owner
            
            db.session.commit()

            return jsonify({'status': 200,
                            'method': 'HTTP PUT',
                            'uri': '/estateapi',
                            'estate_id': estate_.id,
                            'creator_uuid': estate_.creator_uuid,
                            'city': estate_.city,
                            'nb_rooms': estate_.nb_rooms,
                            'description': estate_.description,
                            'rooms_description': estate_.rooms_description,
                            'owner': estate_.owner
                            })

        # The user is not the creator of the entry
        # Operation is forbidden
        else:
            return jsonify({'status': 403,
                            'method': 'HTTP PUT',
                            'uri': '/estateapi',
                            'estate_id': estate_.id,
                            'message': ('Forbidden modification of estate. '
                                        + 'Mismatch between client user and'
                                        + 'estate creator.')
                            })

api.add_resource(EstateAPI, '/estateapi', endpoint='estateapi')


class EstateListAPI(Resource):
    """
    Handles the queries to get estate entry list per city
    Implements GET

    Requirements
    ------------
    3 - Les utilisateurs peuvent consulter uniquement les biens d’une ville 
    particulière

    """

    def get(self, city):
        """
        Returns the list of estate entries located in the city provided as 
        input. Each entry will be the full representation of the entry

        Returns
        -------

        _ : JSON
            List of estate entries located in the city provided as input
        """

        # Get city string
        city_ = city.lower()

        # Filter db based on city
        list_ = Estate.query.filter_by(city=city_).all()

        return jsonify({'status': 200,
                        'method': 'HTTP GET',
                        'uri': '/estateapi',
                        'city': city_,
                        'list of estates in city': str(list_)
                        })

api.add_resource(EstateListAPI, '/estateapi/<string:city>',
                 endpoint='estatelistapi')
