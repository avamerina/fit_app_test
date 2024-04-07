
# Pull base image
FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /app
# Copy project
COPY . /app/
#Install dependenciessqlite3
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
