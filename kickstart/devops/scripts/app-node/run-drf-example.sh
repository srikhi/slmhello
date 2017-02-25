#!/usr/bin/env bash

# TODO:
# - Convert this into a python script.
# - Make the ansible role such that we can develop everything inside a dev container.

set -ux
SCRIPT_NAME=`basename $0`
SCRIPT_DIR=`dirname $0`
SCRIPT_PATH=`readlink -f "${SCRIPT_DIR}"`
DEVOPS_ROOT="${SCRIPT_PATH}/../.."
ANSIBLE_ROOT="${DEVOPS_ROOT}/ansible"
ANSIBLE_PLAYBOOK="${ANSIBLE_ROOT}/launchapp-drf-example.yml"
DEV_SRC_ROOT="${SCRIPT_PATH}/../../.."
# ANSIBLE_BASE_VARS="\"DEV_SRC_ROOT\": \"${DEV_SRC_ROOT}\", \"KICKSEED\": \"1\""
ANSIBLE_BASE_VARS="\"DEV_SRC_ROOT\": \"${DEV_SRC_ROOT}\""
ANSIBLE_BASE_ARGS=" --timeout=60 -v"
ansible-playbook --extra-vars "{ $ANSIBLE_BASE_VARS }" \
    -i localhost,  --sudo \
    --connection=local ${ANSIBLE_PLAYBOOK} \
    --skip-tags="LAUNCH"

sudo docker-compose -f /slm/launchpad/examples/drf/conf/docker-compose.yml up
