#!/usr/bin/env bash

set -ux
# One time dev setup tasks for a bare basic ubuntu machne.
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get -y install python-setuptools python-dev build-essential
sudo apt-get -y install ansible
sudo apt-get -y install cscope
sudo easy_install pip

# Update dev node.
SCRIPT_NAME=`basename $0`
SCRIPT_DIR=`dirname $0`
SCRIPT_PATH=`readlink -f "${SCRIPT_DIR}"`
UPDATE_DEV_NODE="${SCRIPT_PATH}/update.sh"
${UPDATE_DEV_NODE}
