#!/usr/bin/env bash

docker stop blendergrok
docker stop blendergrok
docker rmi opengrok/docker
docker run --name blendergrok -e REINDEX=30 -d -v /Users/priyesh/blender/blender:/opengrok/src -p 8080:8080 opengrok/docker:latest
