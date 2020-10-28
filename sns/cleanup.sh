#!/bin/bash

set -ex

aws cloudformation delete-stack --stack-name airpurifier-avilable-topic --region eu-west-1

