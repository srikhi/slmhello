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
ANSIBLE_PLAYBOOK="${ANSIBLE_ROOT}/setupdevenv.yml"
DEV_SRC_ROOT="${SCRIPT_PATH}/../../.."                                          

ansible-playbook -i localhost,  --sudo  --ask-sudo-pass \
    --connection=local ${ANSIBLE_PLAYBOOK}
