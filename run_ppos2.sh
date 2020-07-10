#!/bin/bash

HOST=ppos2
SSHCONFIG=/home/kmonti/.ssh/config
py.test test_${HOST}*.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.novelpay.pl
