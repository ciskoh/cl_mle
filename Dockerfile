# the base image is a minimal installation of conda https://hub.docker.com/r/continuumio/miniconda3
FROM continuumio/miniconda3:latest

# Update
RUN apt-get update && apt-get upgrade -y

# Avoid writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# install  pip in conda base environment
RUN conda install pip -y

# Install all the dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .
COPY .env .env

# run flask app using gunicorn webserver
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]