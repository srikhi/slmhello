#!/usr/bin/env bash

set -u
SCRIPT_NAME=`basename $0`                                                       
SCRIPT_DIR=`dirname $0`                                                         
SLM_ROOT=`readlink -f "${SCRIPT_DIR}"`                                   
ANSIBLE_BASE_VARS="\"SLM_ROOT\": \"${SLM_ROOT}\""
ANSIBLE_BASE_ARGS=" --timeout=60"
sudo docker-compose -f "$SLM_ROOT/docker-compose.yml" build
ansible-playbook --extra-vars "{ $ANSIBLE_BASE_VARS }" \
    ${ANSIBLE_BASE_ARGS} -i localhost, \
    --sudo  --connection=local \
    ./launch.yml

