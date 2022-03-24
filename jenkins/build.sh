#!/bin/bash

TAG=${BUILD_ID}
DB_USER=${DB_LOGIN_USR}
DB_PASSWORD=${DB_LOGIN_PSW}
DB_ROOT_PASSWORD=${DB_ROOT_PSW}

env
docker-compose -f docker-stack.yml build