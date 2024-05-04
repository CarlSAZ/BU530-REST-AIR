from rest_air import create_app
import sys


app = create_app('config.TestConfig')

if __name__ == "__main__":
    app.run(host='localhost')