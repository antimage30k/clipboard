#!/usr/bin/env bash
set -ex


mkdir -p /var/log/supervisor
mkdir -p /var/log/clipboard
docker-compose -f ./docker-compose.yml up -d