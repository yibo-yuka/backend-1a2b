FROM python:3.12-slim

# 設定工作目錄
WORKDIR /code

# 安裝編譯 PostgreSQL 驅動所需的套件
RUN apt-get update && apt-get install -y libpq-dev gcc

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh

# 複製程式碼
COPY . .

EXPOSE 8000

ENTRYPOINT ["/code/entrypoint.sh"]