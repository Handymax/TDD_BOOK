#!/bin/bash
# re initialize mongodb files

function shutdownDB(){
	PID=$(pgrep mongod)
	if [ $PID ]; then
		kill -2 $PID
	fi
}


shutdownDB
# delet all data files under ~/data/mongo, re-create log dir
rm -rf ~/data/mongodb/*
mkdir ~/data/mongodb/log

# and create qicai21_admin user and qicai21 user
DB_PATH="/home/guodb/data/mongodb"
DB_LOG_PATH="/home/guodb/data/mongodb/log/mongodb.log"

mongod --dbpath $DB_PATH --logpath $DB_LOG_PATH --bind_ip 127.0.0.10 --port 27010 --noauth --fork

# shutdownDB

echo 'mongodb has been re-initialized.'
