#!/usr/bin/env bash

set -u
find . -name *.pyc -delete
find /opt/slm/ -name *.pyc -delete

SCRIPT_NAME=`basename $0`
SCRIPT_DIR=`dirname $0`
SLM_ROOT=`readlink -f "${SCRIPT_DIR}"`                                   
sudo docker stop slmwebapp
sudo docker run -v "$SLM_ROOT/src:/src" slmweb:latest
