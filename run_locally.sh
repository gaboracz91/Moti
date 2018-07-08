#!/usr/bin/env bash

docker build . -t moti
docker run -e MODE='' -e PASSWORD='Potpurizzunk008'\
    --rm -p 8080:8080 moti:latest
