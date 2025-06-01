FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY .env.example .env

# Create necessary directories
RUN mkdir -p logs data data/raw data/processed

# Set permissions
RUN chmod +x src/app.py

# Expose ports
EXPOSE 5000

# Command to run the application
CMD ["python", "src/app.py"]
