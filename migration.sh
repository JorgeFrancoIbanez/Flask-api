#!/bin/bash

source ~/venvs/Flask/bin/activate
export FLASK_APP=cam.py
value=$1
echo $value
if [ $value = '--migrate' ]; then
    echo "migraton in process"
	str="'$*'"
	flask db migrate -m "$str"
elif [ $0 = '--upgrade' ]; then
    echo "upgrade in process"
    flask db upgrade
elif [ $0 = '--downgrade' ]; then
    echo "downgrade in process"
    flask db downgrade
fi