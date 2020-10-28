#!/bin/bash

set -ex

if [[ $# -ne 1 ]] ; then 
  echo "Please provide email address"
  exit -1
fi

EMAIL=$1

sam  deploy --parameter-overrides "NotificationEmail=\"$EMAIL\""
