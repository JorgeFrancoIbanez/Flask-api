#!/bin/bash
virtualenv="Flask";
#export DATABASE_URL=mysql+pymysql://root:root@localhost:3306/col
#install mysql 
#install sudo apt-get install libmysqlclient-dev  or  sudo apt install default-libmysqlclient-dev

export FLASK_APP=cam.py
if [ ! -d "$virtualenv" ]; then
	virtualenv --system-site-packages $virtualenv
	echo virtualenv created;
	source $virtualenv/bin/activate;
	pip install --upgrade setuptools
    sudo apt-get install libmysqlclient-dev python-dev libfreetype6-dev libxft-dev -y
	pip install -r requirements.txt
	echo "requirements were installed";
else
	source "$virtualenv/bin/activate";
	flask run;
fi
