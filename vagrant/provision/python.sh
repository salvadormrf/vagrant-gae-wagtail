#!/bin/bash
export DEBIAN_FRONTEND=noninteractive # remove annoying no stdin warnings

PROJECT_NAME=$1
DJANGO_ENV=$2
PROJECT_DIR=/home/vagrant/$PROJECT_NAME

# install and setup virtualenv, install requirements
pip install virtualenv virtualenvwrapper
su - vagrant -c " \
	export WORKON_HOME=/home/vagrant/.virtualenvs ;\
	export PROJECT_HOME=/home/vagrant/ ;\
	source /usr/local/bin/virtualenvwrapper.sh ;\
	mkvirtualenv $PROJECT_NAME ;\
	workon $PROJECT_NAME ;\
	cd $PROJECT_DIR/project ; make build-deps
"

# set up vagrant user environment
cat << EOF >> /home/vagrant/.bashrc
export DJANGO_ENV=$DJANGO_ENV
export WORKON_HOME=/home/vagrant/.virtualenvs
export PROJECT_HOME=/home/vagrant/
export CLOUDSDK_CORE_PROJECT=your-app-id
source /usr/local/bin/virtualenvwrapper.sh
workon $PROJECT_NAME
EOF