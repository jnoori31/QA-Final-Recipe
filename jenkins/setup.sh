#!/bin/bash

echo "Setup stage"

# apt dependencies
sudo apt-get update
sudo apt-get install -y curl jq python3-venv

# install docker: https://docs.docker.com/engine/install/ubuntu/
if [ ! -f "/usr/bin/docker" ]; then
    sudo apt-get remove docker docker-engine docker.io containerd runc
    sudo apt-get install \
        ca-certificates \
        gnupg \
        lsb-release
    
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null}

    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    # creating a jenkins user and giving it permission to run docker
    sudo usermod -aG docker jenkins
fi

# install docker compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# docker login
docker login --username $DOCKER_LOGIN_USR --password $DOCKER_LOGIN_PSW