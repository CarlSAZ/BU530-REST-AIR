'''This is a basic template for an API App that works with pytest'''
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse


def create_app(config_filename):
    '''Standard Flask API factory pattern'''
    app = Flask(__name__)
    #Optional ability to feed configuration via config file...
    #app.config.from_pyfile(config_filename)
    api = Api(app)
    api.add_resource(BasicApp,"/imu/bno")
    api.init_app(app)
    return app


parser = reqparse.RequestParser()
parser.add_argument('arg0')
parser.add_argument('arg1')


class BasicApp(Resource):
    '''Using the Resource class from flask_restful. 
    Defines the API to access the BasicApp resource'''

    def get(self):
        '''Basic Get method'''
        



if __name__ == "__main__":
    Thisapp = create_app("")
    Thisapp.run(debug=True)
