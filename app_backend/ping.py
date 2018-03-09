from app_backend import api
from flask_restful import Resource
from flask import jsonify


class Ping(Resource):
    """
    Defines the basic test of API responsiveness
    """

    def get(self):
        """
        Returns
        -------

        _ : JSON
            Pong answer
        """
        return jsonify({'status': 200,
                        'method': 'HTTP GET',
                        'uri': '/ping'
                        })

api.add_resource(Ping, '/ping', endpoint='ping')
