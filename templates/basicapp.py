'''This is a basic template for an API App that works with pytest'''
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse


def create_app(config_filename):
    '''Standard Flask API factory pattern'''
    app = Flask(__name__)
    #Optional ability to feed configuration via config file...
    #app.config.from_pyfile(config_filename)
    api = Api(app)
    api.add_resource(BasicApp,"/basicapp/<input0>")
    api.init_app(app)
    return app


parser = reqparse.RequestParser()
parser.add_argument('arg0')
parser.add_argument('arg1')


class BasicApp(Resource):
    '''Using the Resource class from flask_restful. 
    Defines the API to access the BasicApp resource'''

    def get(self,input0):
        '''Basic Get method'''
        return {"data" : "Got Get Request with arg = " + input0}

    def put(self,input0):
        '''Basic put method'''
        data = parser.parse_args()
        # parser will take in the json data and turn it into an object
        # for example, can print out the passed arg0 and arg1
        print(data["arg0"])
        print(data["arg1"])
        return {"data" : "Got Put Request for id = " + input0}, 201

    def delete(self,input0):
        '''Basic '''
        return {"data" : "Got Delete Request for id = " + input0}, 204


if __name__ == "__main__":
    Thisapp = create_app("")
    Thisapp.run(debug=True)
