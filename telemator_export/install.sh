#!/bin/bash

# To be used on distros based on Debian
# Must be run as root

mkdir /etc/nav/python
cp local_urls.py /etc/nav/python/
cp local_settings.py /etc/nav/python/
chown -R nav:nav /etc/nav/python

apt-get -y --no-install-recommends install freetds-dev python3 python3-pip python3-sqlalchemy python3-psycopg2

pip3 install -r requirements.txt
pip install dist/*

python3 main.py
