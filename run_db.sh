#!/bin/bash

HOST=db
SSHCONFIG=/home/kmonti/.ssh/config
py.test test_${HOST}.py test_${HOST}_active.py test_${HOST}_serv.py test_common.py test_ntp.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.novelpay.pl
