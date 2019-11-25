#!/bin/bash

HOST=wf2
SSHCONFIG=./ssh_ntms_config
py.test test_${HOST}*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts 51.77.198.198
