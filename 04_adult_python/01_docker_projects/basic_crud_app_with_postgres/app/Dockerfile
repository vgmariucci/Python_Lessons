# Purpose: Define how to build the backend image

# Use official Python runtime as a parent image
FROM python:3.12-slim

# All subsequent paths are relative to /app inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Uvicorn will be listen on port 8000
EXPOSE 8000

# Command is overridden in docker-compose for dev (with --reload)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]