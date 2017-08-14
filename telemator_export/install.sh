#!/bin/bash

# To be used on distros based on Debian
# Must be run as root

apt-get -y --no-install-recommends install freetds-dev python3 python3-pip python3-sqlalchemy python3-psycopg2 python3-pandas

pip3 install -r requirements.txt

python3 main.py
