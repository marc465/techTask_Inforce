FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=your_database_name \
    DB_USER=your_database_user \
    DB_PASSWORD=your_database_password

CMD ["python", "main.py"]
