FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create temporary directory for Prometheus
RUN mkdir -p /tmp && chmod 777 /tmp

# Copy application code
COPY . .

# Set port
EXPOSE 8000

# Run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
