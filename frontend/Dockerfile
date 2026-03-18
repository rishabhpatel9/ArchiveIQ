FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Reflex (sqlite, etc.)
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000
CMD ["reflex", "run", "--env", "prod", "--frontend-port", "3000"]
