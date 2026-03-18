FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Match the port in docker-compose
EXPOSE 5678

CMD ["python", "api/main.py"]
