# Base image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files (including Makefile and requirements.txt)
COPY . .

# Install Python dependencies via Makefile
RUN make install

# Expose the app port
EXPOSE 8000

# Use Makefile to run the app
CMD ["make", "run"]
