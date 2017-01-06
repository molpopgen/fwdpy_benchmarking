#!/bin/bash

parallel ./runslim.sh scriptLargeN2.txt :::: seeds 
parallel ./runslim.sh scriptLargeN1.txt :::: seeds
#
##This is fwdpp 0.5.0, which is same run-time performance as 0.4.7 (Slim paper tests vs 0.4.6, which is slower).
#for i in $(seq 1 1 5)
#do
#    seed=`head -n $i seeds | tail -n 1`
#    echo $seed
#    /usr/bin/time -f "%e %M" -o fwdpp1000.$seed.time ~/src/fwdpp/examples/diploid_ind 10000 1000 1000 100000 10 1 $seed &
#    /usr/bin/time -f "%e %M" -o fwdpp10000.$seed.time ~/src/fwdpp/examples/diploid_ind 10000 10000 10000 100000 10 1 $seed &
#done
#

