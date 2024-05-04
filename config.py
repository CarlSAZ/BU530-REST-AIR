

class BaseConfig(object):
    CONTACT = {'name': 'Carl Stevenson',
               'url': 'https://github.com/CarlSAZ/BU530-REST-AIR',
               'email': "carl4ece@bu.edu"}
    LICENSE = {'name': 'Apache 2.0',
               'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'}

class TestConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
    REDIS_URL = "redis://127.0.0.1:6379/0"


class DevConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = False
    REDIS_URL = "redis://airship-server:6379/0"