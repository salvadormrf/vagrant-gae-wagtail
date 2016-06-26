#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive # remove annoying no stdin warnings

set -ex

apt-get update
apt-get upgrade -y
apt-get install --no-install-recommends -y -q \
	language-pack-en git

apt-get -y install build-essential
apt-get -y install libffi-dev libssl-dev
apt-get -y install python-dev python-pip git

# for Pillow
apt-get -y install libjpeg-dev
ln -sf /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
ln -sf /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
ln -sf /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# Install project dependencies
apt-get install --no-install-recommends -y \
	unzip \
	libjpeg8 \
	libjpeg62-dev \
	libfreetype6 \
	libfreetype6-dev \
	libmysqlclient-dev \
	gettext \
	imagemagick \
	graphicsmagick
