#!/bin/bash

cd load_test
for i in {1..10}
do
   echo "=== Running $i load test ==="
   npx cypress run &
done
