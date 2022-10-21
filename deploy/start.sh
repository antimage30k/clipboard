#!/usr/bin/env bash

chmod -R o+rwx /var/www/clipboard

cp /var/www/clipboard/deploy/clipboard.conf /etc/supervisor/conf.d/clipboard.conf

# 初始化
cd /var/www/clipboard

# 启动服务
supervisord -c /etc/supervisor/supervisord.conf

tail -f /dev/null