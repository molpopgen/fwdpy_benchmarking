#!/bin/bash

/usr/bin/time -f "%e %M" -o $1.$2.time ~/src/SLiM/bin/slim -seed $2 $1
