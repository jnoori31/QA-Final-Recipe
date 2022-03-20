#!/bin/bash

echo "Deploy stage"

scp docker-stack.yaml jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com:/home/jenkins/docker-stack.yaml
ssh jenkins@swarm-deployment-server.uksouth.cloudapp.azure.com 'docker stack deploy --compose-file docker-stack.yaml qa-recipe'