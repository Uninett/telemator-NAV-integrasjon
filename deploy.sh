#!/bin/sh
# -----------------------------------------------------------------------
# Shell script to deploy telemator-NAV-integrasjon
#
# Created by Vegard Vesterheim (<vegardv@uninett.no>) 2018-06-15
# -----------------------------------------------------------------------
#set -x # Uncomment to debug

gitrepo='git@scm.uninett.no:verktoy/telemator-NAV-integrasjon.git'
srcdir=~/src

cd $srcdir
git clone $gitrepo || cd telemator-NAV-integrasjon ; git pull
git checkout master
cd telemator-NAV-integrasjon
rm dist/*

# FIXME
# Must copy local_urls.py, local_settings.py also

python ./setup.py build sdist
sudo pip install dist/*
sudo apachectl graceful

