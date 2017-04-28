#!/usr/bin/env bash

THETA=$1
RHO=$2
SEED=$3

/usr/bin/time -f "%e %M" -o fwdpy.$THETA.$RHO.$SEED.time.txt python3 run_fwdpy.py $THETA $RHO $SEED
