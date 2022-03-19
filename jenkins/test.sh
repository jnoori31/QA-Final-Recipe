#!/bin/bash

echo "Test stage"

# venv created, sourced
python3 -m venv venv
source venv/bin/activate

# install pip dependencies
pip3 install pytest pytest-cov flask_testing requests_mock
pip3 install -r requirements.txt

# run pytest frontend
python3 -m pytest --cov

# remove venv
deactivate
rm -rf venv