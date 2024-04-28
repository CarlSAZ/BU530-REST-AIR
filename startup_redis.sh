#!/bin/bash
# Create the network (TODO: check if network already exists)
docker network create redisnetwork
# Launch the redis server with correct ports and name
# This is setup so that only the local host will be able to access the port with the redis server. 
docker run -p 127.0.0.1:6379:6379 -it --rm --network redisnetwork --name airship-server redis/redis-stack-server