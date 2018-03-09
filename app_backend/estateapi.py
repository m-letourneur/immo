from app_backend import api, db
from flask_restful import Resource
from flask import jsonify, request
from models.user import User, Estate


class EstateAPI(Resource):
    """
    Handles the queries to create and modify estate entries

    Requirements
    ------------
    1 - Un utilisateur peut modifier les caractéristiques d’un bien (changer 
    le nom, ajouter une pièce, etc… )

    2 - Un propriétaire ne peut modifier que les caractéristiques de son bien 
    sans avoir accès à l’édition des autres biens.

    3 - Les utilisateurs peuvent consulter uniquement les biens d’une ville 
    particulière

    """

    def get(self):
        """
        Returns the list of estate entries located in the city provided as 
        input. Each entry will be the full representation of the entry
        
        Returns
        -------

        _ : JSON
            List of estate entries located in the city provided as input
        """

        # Get city string
        city_ = request.json.get('city')

        # Filter db based on city
        list_ = Estate.query.filter_by(city=city_.lower()).all()
        
        return jsonify({'status': 200,
                'method': 'HTTP GET',
                'uri': '/estatepi',
                'city': city_.lower(),
                'list of estates in city': list_
                })


    def post(self):
        """
        Creation of an estate entry by any user

        Returns
        -------

        _ : JSON
            Validation of creation

        """

    def put(self):
        """
        Creation of an estate entry by only allowed for the user that has 
        created it

        Returns
        -------

        _ : JSON
            Validation of modification

        """

api.add_resource(EstateAPI, '/estateapi', endpoint='estateapi')
