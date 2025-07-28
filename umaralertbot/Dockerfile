# Use official Python 3.11 image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (for keepalive)
EXPOSE 8080

# Run the app
CMD ["python", "main.py"]
