#!/bin/bash

HOST=beta
SSHCONFIG=/home/kamil/.ssh/config
py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.novelpay.pl
