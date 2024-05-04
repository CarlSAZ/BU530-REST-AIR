
from apiflask import APIBlueprint, HTTPBasicAuth

# TODO: Find a better way than circular importing...
from rest_air import rdb, auth
from flask import current_app
landing = APIBlueprint('landing',__name__,url_prefix='/')

@auth.verify_password
def verify_password(username,password):
    '''TBD: Better define authentication'''
    if(username=='admin' and password=='tacocat'):
        return username

@landing.get('/')
def index():
    return {'message': 'hello human! This is a flying airship!'}

@landing.get('/sensors')
def list_sensors():
    return {''}



@landing.route('/killswitch',methods=['GET','POST','PUT'])
@landing.auth_required(auth)
def send_killswitch_sig():
    return {'message':'sent killswitch signal. '}