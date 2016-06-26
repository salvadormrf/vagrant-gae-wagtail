#!/bin/bash

export CLOUDSDK_PYTHON_SITEPACKAGES=1
export CLOUDSDK_COMPONENT_MANAGER_FIXED_SDK_VERSION=0.9.63

# Install Google Cloud SDK

echo "Installing Google Cloud SDK"
cd /opt

wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip \
	&& unzip google-cloud-sdk.zip \
	&& rm google-cloud-sdk.zip

./google-cloud-sdk/install.sh \
	--usage-reporting=false \
	--rc-path=/home/vagrant/.profile \
	--bash-completion=false \
	--path-update=true \
	--additional-components app-engine-python preview app alpha beta


# Patches appengine file watcher to avoid watching for node_modules and vendor paths.
echo """

_IGNORED_DIRS = ('node_modules', 'vendor',)
def skip_ignored_dirs(dirs):
  _remove_pred(dirs, lambda d: d.startswith(_IGNORED_PREFIX) or d in _IGNORED_DIRS)

""" >> /opt/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/watcher_common.py
