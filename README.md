# REST-AIR - A Boston University EC530 course final project

The purpose of this repository is firstly to learn the fundamentals of modern software engineering.

The code here aims to implement a REST API interface for a robotic airship. With this code running on the airship, it will provide an external interface for a user to send navigation commands, get sensor data, and perform other allowed actions. This allows the user to connect from any application and develop a web client or mobile application.

## How to initialize REDIS Server

This project suggests the use of the REDIS docker containers to run a database.

Use the following to launch the redis stack server container (which includes the timeseries module)
docker run -p 6379:6379 -it --rm redis/redis-stack-server
