#!/bin/bash

export TAG=${BUILD_ID}
export DB_USER=${DB_LOGIN_USR}
export DB_PASSWORD=${DB_LOGIN_PSW}
export DB_ROOT_PASSWORD=${DB_ROOT_PSW}

env
docker-compose -f docker-stack.yml build