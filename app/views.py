from flask import make_response, jsonify
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return make_response(
            jsonify({
                "message": "Hello world in Flask"
            }, 200)
        )
