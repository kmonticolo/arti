#!/bin/bash

HOST=db2
SSHCONFIG=./ssh_ntms_config
py.test test_db2*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts 51.77.198.199
