#!/bin/bash

echo "Deploy stage"

# -o flag, as we are sshing to server for first time
scp -o 'StrictHostKeyChecking no' \
    docker-stack.yml \
    jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com:/home/jenkins/docker-stack.yml

scp -o 'StrictHostKeyChecking no' \
    nginx/nginx.conf \
    jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com:/home/jenkins/nginx.conf


ssh -o 'StrictHostKeyChecking no' \
    jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com \
    BUILD_ID=${BUILD_ID} \
    docker stack deploy --compose-file docker-stack.yml qa-recipe