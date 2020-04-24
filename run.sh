#!/bin/bash

docker run -ti \
        --rm \
        -p 4200:4200/tcp \
        --env-file=.env \
        aamillan/plex-webhook:latest
