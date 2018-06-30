#!/usr/bin/env bash

docker build . -t moti
docker run -e MODE='' \
    --rm -p 8080:8080 moti:latest
