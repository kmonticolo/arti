#!/bin/bash

HOST=ppos
SSHCONFIG=/home/kmonti/.ssh/config
py.test test_ppos_active.py  test_ppos.py  test_ppos_serv.py test_common.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.novelpay.pl
