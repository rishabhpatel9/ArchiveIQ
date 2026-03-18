FROM python:3.10-slim

WORKDIR /app

# Install uv
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY . .

# Match the port in docker-compose
EXPOSE 5678

CMD ["uv", "run", "python", "api/main.py"]
