FROM ubuntu:18.04

MAINTANER Your Name "moses@cisco.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /heimdal

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]