#!/bin/bash

EXPECTED_ARGS=2
MYSQL=`which mysql`

if [[ $# -ne EXPECTED_ARGS ]]; then
    echo "Usage: $0 db_name db_user"
    exit
fi

Q1="CREATE DATABASE IF NOT EXISTS $1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;"
Q2="GRANT ALL PRIVILEGES ON $1.* to '$2'@'localhost';"
Q3="FLUSH PRIVILEGES;"

$MYSQL -u root -e "${Q1}${Q2}"
