FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    apt-get install -y build-essential && \
    # ffmpeg
    apt-get install -y ffmpeg libavcodec-extra && \
    pip install grpcio==1.33.2
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt
COPY . .
