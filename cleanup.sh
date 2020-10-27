#!/bin/bash

set -ex

docker run --rm -ti --user `id -u`:`id -g` -v ~/.aws:/.aws -v $(pwd):/aws amazon/aws-cli cloudformation delete-stack --stack-name check-airpurif-avail --region eu-west-1

