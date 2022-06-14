#!/bin/bash


docker run -d -h local --platform linux/amd64 -p 8000:8000 --env-file .env statistic-backend:latest