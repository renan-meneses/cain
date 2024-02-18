# Pull base image
FROM python:3.10.2-slim-bullseye

# Set work directory
WORKDIR /usr/src/app

# Copy project
COPY . .

RUN apt-get update
RUN apt-get install build-essential -y
RUN pip install --upgrade pip

# Install dependencies
RUN pip install gunicorn uvicorn
RUN pip install -r requirements.txt

CMD ["./prestart.sh"]