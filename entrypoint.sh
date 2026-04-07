#!/bin/sh

echo "Waiting for postgres..."

# 使用 python 嘗試連接資料庫，直到成功為止
# 這樣就不需要安裝 nc 了
python << END
import socket
import time
import os

host = os.environ.get('DB_HOST', 'db')
port = int(os.environ.get('DB_PORT', 5432))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error:
        time.sleep(0.1)
END

echo "PostgreSQL started"

# 執行遷移
python manage.py migrate

# 啟動伺服器
python manage.py runserver 0.0.0.0:8000