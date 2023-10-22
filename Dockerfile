# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Install dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
        netcat \
	&& rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the Django application
CMD ["/bin/bash", "/app/entrypoint.sh"]
