#!/usr/bin/env bash

apt-get install -y python3 python3-pip python3-dev python3-setuptools

pip3 install --upgrade pip

pip3 install -r /autograder/source/requirements.txt

pip3 install numpy

pip3 install --upgrade pillow

pip3 install matplotlib


