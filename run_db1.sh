#!/bin/bash

HOST=db1
SSHCONFIG=./ssh_ntms_config
py.test test_db1*.py test_common.py test_ntp.py --ssh-config=${SSHCONFIG} $@ --hosts 192.99.119.27
