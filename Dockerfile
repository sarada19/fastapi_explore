# Use official Python image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ENVIRONMENT=staging

# Set working directory
WORKDIR /app

# Upgrade system packages to address vulnerabilities
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 👇 Copy the entire 'project' folder into /app/
COPY project ./project

# Or if main.py is outside project/, then:
# COPY main.py /app/
# COPY project /app/project

EXPOSE 8080

# Default command
CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8080"]