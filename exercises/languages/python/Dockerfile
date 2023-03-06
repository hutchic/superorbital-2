# Stage 1: Build dependencies
FROM python:3.9-slim-buster AS build

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Copy dependencies and project files
FROM python:3.9-slim-buster

# Copy dependencies from build stage
COPY --from=build /install /usr/local

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/

# Set entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["python", "drone_cli.py"]
