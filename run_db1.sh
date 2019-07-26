#!/bin/bash

HOST=db1
SSHCONFIG=./ssh_ntms_config
py.test test_1db*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts 192.99.119.27
