#!/bin/bash


docker build -f develop.dockerfile -t statistic-backend .
createdb statistic
./env/bin/alembic upgrade head
cp dev.env .env
echo "Successful prepared docker image"
