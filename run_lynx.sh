#!/bin/bash

HOST=lynx
SSHCONFIG=/home/kmonti/.ssh/config
py.test test_${HOST}*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.artifact.pl
