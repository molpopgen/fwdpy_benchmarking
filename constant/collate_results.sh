#!/bin/env bash

for i in 1000 10000
do
    echo "time mem" > fwdpy11_results.$i.txt
    cat fwdpy.$i.$i.*.time.txt >> fwdpy11_results.$i.txt
done

echo "time mem" > slim.1000.txt
cat scriptLargeN2.txt.*.time >> slim.1000.txt

echo "time mem" > slim.10000.txt
cat scriptLargeN1.txt.*.time >> slim.10000.txt
