#!/bin/bash

EMAIL='test@test.pl'
if [[ $# -gt 0 ]] ; then 
  EMAIL=$1
fi

set -ex

sam local invoke --event events/event.json --parameter-overrides "NotificationEmail=\"$EMAIL\" PurifierModelName=\"AC1217\""
