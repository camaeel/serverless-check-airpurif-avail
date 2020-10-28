#!/bin/bash

set -ex

sam local invoke --event events/event.json --parameter-overrides 'NotificationEmail="test@test.pl" PurifierModelName="AC3059"'
