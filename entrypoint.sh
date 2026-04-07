#!/bin/sh

# 等待資料庫就緒 (這是一個簡單的循環檢查)
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# 執行遷移
python manage.py migrate

# 啟動伺服器
python manage.py runserver 0.0.0.0:8000