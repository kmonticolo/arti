#!/bin/bash

HOST=amq1
SSHCONFIG=./ssh_ntms_config
py.test test_${HOST}*.py test_common.py test_ntp.py --ssh-config=${SSHCONFIG} $@ --hosts 192.99.119.25
