# Use a base image with Python and LibreOffice
FROM python:3.10-slim

# Install LibreOffice and dependencies
RUN apt-get update && apt-get install -y \
    libreoffice \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the uploads folder
RUN mkdir -p uploads

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
