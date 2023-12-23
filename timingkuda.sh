#!/bin/bash
docker build -t hell . --no-cache
sleep 30
docker rmi hell
sleep 30
