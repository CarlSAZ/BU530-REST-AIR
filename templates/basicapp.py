'''This is a basic template for an API App that works with pytest'''
from apiflask import APIFlask

app = APIFlask(__name__, title='Basic Template')

@app.get('/')
def index():
    return {'message': 'hello'}

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
