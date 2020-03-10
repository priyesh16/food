#!/usr/bin/env bash

docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
docker run -td --name food -v /Users/priyesh/food/src/:/src/  -v /Users/priyesh/food/bld/:/bld/ priyesh/food:1.0
docker exec -it food /src/startup.sh
