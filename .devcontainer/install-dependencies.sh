#!/bin/bash

# install or upgrade pip
python -m ensurepip --upgrade

# install core dependencies
pip install -r requirements.txt

# install test dependencies
pip install -r requirements-test.txt

# install GitHub Actions emulator (act)
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
