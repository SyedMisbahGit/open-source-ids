#!/bin/bash

# Initialize database
alembic upgrade head

# Create necessary directories
mkdir -p logs data data/raw data/processed

# Start services
make start-all
