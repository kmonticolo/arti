#!/bin/bash

HOST=front2
SSHCONFIG=./ssh_ntms_config
py.test test_${HOST}*.py test_common.py test_ntp.py --ssh-config=${SSHCONFIG} $@ --hosts 51.77.198.196
