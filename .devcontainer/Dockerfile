# Use an official Python base image from the Docker Hub
FROM python:3.10

# Install utilities
RUN apt-get update && apt-get install -y curl wget git iputils-ping

# Declare working directory
WORKDIR /apps