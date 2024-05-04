
from apiflask import APIBlueprint, HTTPBasicAuth

# TODO: Find a better way than circular importing...
from rest_air import rdb, auth
from flask import current_app
landing = APIBlueprint('landing',__name__,url_prefix='/')

@auth.verify_password
def verify_password(username,password):
    '''TBD: Better define authentication'''
    print(f"Logging in as {username}, {password}")
    if(username=='admin' and password=='tacocat'):
        return username

@landing.get('/')
def index():
    return {'message': 'hello human! This is a flying airship!'}

@landing.get('/sensors')
def list_sensors():
    return {''}

