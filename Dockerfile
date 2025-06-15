# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask app on port 8080
ENV PORT 8080

# Run the Flask app
CMD ["python", "app.py"]