#!/bin/bash

HOST=draco
SSHCONFIG=/home/kamil/.ssh/config
py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} $@ --hosts ${HOST}.artifact.pl
