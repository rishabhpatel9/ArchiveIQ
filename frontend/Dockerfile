FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Reflex (sqlite, etc.)
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY . .

EXPOSE 3000
CMD ["uv", "run", "reflex", "run", "--env", "prod", "--frontend-port", "3000"]
