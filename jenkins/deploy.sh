#!/bin/bash

echo "Deploy stage"

# -o flag, as we are sshing to server for first time
scp -o 'StrictHostKeyChecking no' \
    docker-stack.yml \
    jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com:/home/jenkins/docker-stack.yml

ssh -o 'StrictHostKeyChecking no' \
    jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com \
    'docker stack deploy --compose-file docker-stack.yml qa-recipe'