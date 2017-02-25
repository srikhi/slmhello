#!/usr/bin/env bash

set -xu
find . -name *.pyc -delete
find /opt/crud/ -name *.pyc -delete
SCRIPT_NAME=`basename $0`                                                       
SCRIPT_DIR=`dirname $0`                                                         
CRUD_ROOT=`readlink -f "${SCRIPT_DIR}"`                                   
ANSIBLE_BASE_VARS="\"CRUD_SRC_ROOT\": \"${CRUD_ROOT}/crud\""
ANSIBLE_BASE_ARGS=" --timeout=60"
ansible-playbook --extra-vars "{ $ANSIBLE_BASE_VARS }" \
    ${ANSIBLE_BASE_ARGS} -i localhost, \
    --sudo  --connection=local \
    $CRUD_ROOT/launchcrudwebapp.yml --skip-tags="LAUNCH"

sudo docker-compose -f /opt/crudev/conf/crudwebapp-compose.yml up

