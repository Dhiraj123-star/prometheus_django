# -----------------------------
# Stage 1: Base image
# -----------------------------
FROM python:3.12-slim AS base

# Prevent Python from writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (psycopg2, build tools if needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Stage 2: Install dependencies
# -----------------------------
FROM base AS builder

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Stage 3: Final runtime image
# -----------------------------
FROM base

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy Django project code
COPY . .

# Expose Django port
EXPOSE 8000

# Default command -> run server (can override in docker-compose or k8s)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
