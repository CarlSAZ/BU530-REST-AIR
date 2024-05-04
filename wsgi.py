from rest_air import create_app
import sys

if len(sys.argv) >0:
    configtype = sys.argv[1]
else:
    configtype = 'config.DevConfig'

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost')