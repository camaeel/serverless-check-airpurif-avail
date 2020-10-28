#!/bin/bash

set -ex

aws cloudformation delete-stack --stack-name check-airpurif-avail --region eu-west-1

