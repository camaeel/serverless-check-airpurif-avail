#!/bin/bash

if [[ $# -ne 1 ]] ; then 
  echo "Please provide email address"
  exit -1
fi

EMAIL=$1

set -ex

aws cloudformation create-stack  --stack-name airpurifier-avilable-topic --template-body "`cat sns-cf.yml`" --parameters "ParameterKey=AirPurifierAvailableNotificationEmail,ParameterValue=$EMAIL,UsePreviousValue=false" --tags 'Key=project,Value=serverless-check-airpurifier-availability' --region eu-west-1

# --on-failure DELETE
