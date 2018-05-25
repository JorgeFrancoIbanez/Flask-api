#!/bin/bash


#export DATABASE_URL=mysql+pymysql://root:root@localhost:3306/col
export FLASK_APP=cam.py
source ~/venvs/Flask/bin/activate
flask run
