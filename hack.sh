#!/bin/sh

# Waiting for DB
waiting() {
    while ! nc -z $1 $2;
    do
        echo "Waiting for $1:$2 ... "
        sleep 1
    done
}

waiting redis_dc 6379
waiting mysql_dc 3306

# Init
PORT=$1
SETTING=$2
CRT_FILE=$3
KEY_FILE=$4

DEV_SETTING_PATH="LittleServer.settings.dev"
PROD_SETTING_PATH="LittleServer.settings.prod"
CMD="python manage.py"
MOD=""
SETTING_CHOICE=""
ARGS=""

case $SETTING in
    "DEV")
        MOD="runserver"
        CHOICE="--settings=$DEV_SETTING_PATH"
    ;;
    "PROD")
        MOD="runserver"
        CHOICE="--settings=$PROD_SETTING_PATH"
    ;;
    "PROD-SSL")
        MOD="runserver_plus"
        CHOICE="--settings=$PROD_SETTING_PATH"
        ARGS="--cert-file=$CRT_FILE --key-file=$KEY_FILE"
    ;;
esac

$CMD makemigrations $CHOICE || true
$CMD migrate $CHOICE

$CMD $MOD 0.0.0.0:$PORT $CHOICE $ARGS