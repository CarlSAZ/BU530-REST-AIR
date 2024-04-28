#!/bin/bash
docker network create redisnetwork
docker run -p 127.0.0.1:6379:6379 -it --rm --network redisnetwork --name airship-server redis/redis-stack-server