#!/bin/bash

# set -ex

TOPIC=`aws cloudformation list-exports --query "Exports[?Name == 'airpurifier-avilable-topic-TopicARN'].Value | [0]"`

echo "TOPIC=$TOPIC"
echo  "{ \"CheckPurifAvailFunction\": {\"NOTIFICATION_TOPIC\": $TOPIC}}" > events/env.json


set -ex

sam local invoke --event events/event.json --parameter-overrides "PurifierModelName=\"AC1217\"" -n events/env.json
