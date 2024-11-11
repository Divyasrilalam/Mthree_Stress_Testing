# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY stress1.py .

RUN pip install psutil

# Install required packages
RUN apt-get update && \
    apt-get install -y stress-ng iperf3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Command to run the script when the container starts
CMD ["python", "stress1.py"]