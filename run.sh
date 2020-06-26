#!/usr/bin/env bash

# build with redirect to stderr
make build 1>&2

make run 1>&2

sleep 2

curl http://localhost:5000/plain

make stop 1>&2
