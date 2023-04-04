FROM python:3.11.2-buster

RUN mkdir -p /app

# Dependencies
WORKDIR /app
COPY ./docker/build.sh /app/
RUN chmod +x /app/build.sh
RUN chmod 777 /app/build.sh
RUN /app/build.sh

# App
COPY ./backend/ /app/
COPY ./docker/run* /app/
RUN chmod -R 777 /app
