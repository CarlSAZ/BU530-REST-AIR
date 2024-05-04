'''Unit tests for the basic app module that uses flask_restful'''
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import logging
import pytest
from rest_air import create_app
from fakeredis import FakeRedis

log = logging.getLogger('Test.bno_imu')

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

# For example, this function wants a client app to be passed in. Pytest will recognize
# that we defined a fixture for this, and will call fixture_client to make it on the spot
# for us (which will in turn call fixture_app). 
def test_basicapp_get(client):
    '''This tests the get function by sending a get request. The url is defined 
    from the base URL of the app. In this case basicapp resource was created at 
    /basicapp. No localhost or ports needed'''
    log.info("Testing a get")
    response = client.get("/sensors/imu")
    assert response.status_code == 200


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # The function pytest.main() will run as if running pytest from command line
    # This is the best way to get fixtures to work from running a script...
    # As they don't get passed directly if called...
    # passing __file__ as an argument will prevent pytest from running every single
    # test script in our working directory too
    pytest.main([__file__])
