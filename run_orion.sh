#!/bin/bash

HOST=orion
SSHCONFIG=/home/kmonti/.ssh/config
py.test test_${HOST}*.py test_common.py test_ntp.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.artifact.pl
