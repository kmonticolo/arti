#!/bin/bash

HOST=front1
SSHCONFIG=./ssh_ntms_config
py.test test_${HOST}*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts 192.99.119.24
