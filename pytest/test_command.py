'''Unit tests for the basic app module that uses flask_restful'''
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import logging
import pytest
from rest_air import create_app
import base64

log = logging.getLogger('Test.commands')

# fixtures work by defining steps to setup a required environment for
# test functions. They can be called in the input arguments, and pytest
# will execute the fixture code during the argument passing (I think)
# yield seems to be used so that a code block after it executes after the test
# function calling it is complete.
# Other thing to note: The name argument in the pytest.fixture(name="foo") should match
# the argument in the other functions to be used. By defualt, this is the same as the fixture's 
# function name. But that results in pytest giving warnings about overriding... So this way is 
# more pythonic.
@pytest.fixture(name='app')
def fixture_app():
    '''Initializes the app'''
    # Start of initialization block
    #newapp = create_app(config_object='config.PyTestConfig',custom_redis=FakeRedis())
    newapp = create_app(config_object='config.TestConfig')
    # END of initialization block
    yield newapp
    # any teardown or destruction code can go here after yield (same for other fixtures)

@pytest.fixture(name='client')
def fixture_client(app):
    '''Returns a test client that can be used for testing'''
    yield app.test_client()

@pytest.fixture(name='runner')
def fixture_runner(app):
    '''Not sure what a cli runner is yet, but this creates it...'''
    yield app.test_cli_runner()

@pytest.fixture(name='auth_header')
def authenticate_client():
    credentials = base64.b64encode(b"admin:tacocat")
    yield {"Authorization": "Basic {}".format(credentials.decode('utf-8'))}
    #yield {"httpCredentials": {"username": 'admin', "password":'tacocat'}}

def test_command_killswitch_nologin(client):
    '''This tests the get function by sending a get request. The url is defined 
    from the base URL of the app. In this case basicapp resource was created at 
    /basicapp. No localhost or ports needed'''
    log.info("Testing a killswitch put")
    response = client.post("/command/killswitch")
    assert response.status_code == 401

def test_command_killswitch(client,auth_header):
    '''This tests the get function by sending a get request. The url is defined 
    from the base URL of the app. In this case basicapp resource was created at 
    /basicapp. No localhost or ports needed'''
    log.info("Testing a killswitch put")
    response = client.post("/command/killswitch",headers=auth_header)
    assert response.status_code == 200
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # The function pytest.main() will run as if running pytest from command line
    # This is the best way to get fixtures to work from running a script...
    # As they don't get passed directly if called...
    # passing __file__ as an argument will prevent pytest from running every single
    # test script in our working directory too
    pytest.main([__file__])

