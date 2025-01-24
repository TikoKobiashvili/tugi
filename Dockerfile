# Use an official Python image as the base
FROM python:3.12-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /opt/app

# Copy only the necessary files
COPY app/ ./app/
COPY requirements/dev.txt ./

# Install dependencies
RUN pip install --no-cache-dir --progress-bar off -r dev.txt

# Exclude unnecessary files by not copying everything from the host

# Expose the service port
EXPOSE 8041

# Define the command to run the service
# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8041", "--reload"]