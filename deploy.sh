#!/bin/sh
git pull origin main
docker-compose -f docker-compose-deploy.yml up --build
