#!/usr/bin/env bash
set -ex


mkdir -p /home/log/supervisor
mkdir -p /home/log/clipboard
docker-compose -f ./docker-compose.yml up -d