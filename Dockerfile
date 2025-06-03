# Use official Python image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Upgrade system packages to address vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Run the app (change if you want to run differently)
CMD ["python", "app.py"]
