# Dockerfile

# Use official Python 3.11 as base
FROM python:3.11-slim

WORKDIR /app

# Copy bot files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Web port for keepalive (optional)
EXPOSE 8080

# Run the bot
CMD ["python", "main.py"]

