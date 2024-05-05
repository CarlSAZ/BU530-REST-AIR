# REST-AIR - A Boston University EC530 course final project

The purpose of this repository is firstly to learn the fundamentals of modern software engineering.

The code here aims to implement a REST API interface for a robotic airship. With this code running on the airship, it will provide an external interface for a user to send navigation commands, get sensor data, and perform other allowed actions. This allows the user to connect from any application and develop a web client or mobile application.

## Accessing the OpenAPI documentation

Most of the documentation for the API is self documenting via OpenAPI specifications. These documents will provide coverage of all valid endpoints, and valid methods for interaction. Otherwise the markdown pages within this repository will focus on design methodology and purpose as needed, and will not redocument the API methods.

Once the application is running, the endpoint of /docs will provide an interactive documentation of the various HTTP methods and input/output schemas
i.e. http://127.0.0.1:500/docs

Alternatively, the following swaggerhub page is available to browse the API documentation. It is not garunteed to be in sync with development, and only 
shows the latest API version. Accessing the openapi doc from a running instance is more reliable.

<https://app.swaggerhub.com/apis-docs/CarlStevenson-ed8/REST-AIR/0.1.0>

## How to initialize REDIS Server

This project is meant to run on an embedded robot (currently in development [here](https://github.com/CarlSAZ/bu_ec601_Sonic_Airship)). One part of this is a reliance on a redis server that collects timeseries data, and accessible by both this API and the ROS modules. 

This project suggests the use of the REDIS docker containers to run a database. Use the shell script startup_redis.sh or copy the following to launch the redis stack server container (which includes the timeseries module)

docker run -p 6379:6379 -it --rm --network redisnetwork --name airship-server redis/redis-stack-server

### Simulating the robot REDIS inputs

To test this server without the robot running, a few test scripts have been made to simulate inputs to the redis server. While the REDIS server is up and running, the python scripts under </simulator_scripts> can be run to create entry data.

## How to start flask server

To run the server as intended with docker, the official image can be pulled from dockerhub. An example of how to start up the image is given as a shell script in <start_rest_air.sh>. The command is copied below to explain it's use. The main aspect is setting up the port for the flask server to bind to externally. The second number (5002) in the -p argument is most important, as this is the internal port configured for the flask server. The network name "redisnetwork" is also critical and needs to reflect the docker network name in use by the redis container (see above)

docker run -p 5000:5002 -it --rm --network redisnetwork --name rest-air robollama/bu530-rest-air:main

Or run the flask application without using docker (not recommended for production or on the robot), navigate to the root folder of the repo and run

flask run

