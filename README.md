# REST-AIR - A Boston University EC530 course final project

The purpose of this repository is firstly to learn the fundamentals of modern software engineering.

The code here aims to implement a REST API interface for a robotic airship. With this code running on the airship, it will provide an external interface for a user to send navigation commands, get sensor data, and perform other allowed actions. This allows the user to connect from any application and develop a web client or mobile application.

## How to initialize REDIS Server

This project suggests the use of the REDIS docker containers to run a database.

Use the shell script startup_redis.sh or copy the following to launch the redis stack server container (which includes the timeseries module)

docker run -p 6379:6379 -it --rm --network redisnetwork --name airship-server redis/redis-stack-server

## How to start flask server

To run the server as intended with docker, the official image can be pulled from dockerhub. An example of how to start up the image is given as a shell script in <start_rest_air.sh>. The command is copied below to explain it's use. The main aspect is setting up the port for the flask server to bind to externally. The second number (5002) in the -p argument is most important, as this is the internal port configured for the flask server. The network name "redisnetwork" is also critical and needs to reflect the docker network name in use by the redis container (see above)

docker run -p 5000:5002 -it --rm --network redisnetwork --name rest-air robollama/bu530-rest-air:main

Or run the flask application without using docker (not recommended for production or on the robot), navigate to the root folder of the repo and run

flask run

## Accessing the OpenAPI documentation

Once the application is running, the endpoint of /docs will provide an interactive documentation of the various HTTP methods and input/output schemas
i.e. http://127.0.0.1:500/docs

Alternatively, the following swaggerhub page is available to browse the API documentation. It is not garunteed to be in sync with development, and only 
shows the latest API version. Accessing the openapi doc from a running instance is more reliable.

<https://app.swaggerhub.com/apis-docs/CarlStevenson-ed8/REST-AIR/0.1.0>
