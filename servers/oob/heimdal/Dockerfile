FROM ubuntu:18.04

MAINTAINER Moses Frost "moses@cisco.com"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /heimdal/requirements.txt

WORKDIR /heimdal

RUN pip3 install -r requirements.txt

COPY . /heimdal

expose 80 443
#ENTRYPOINT [ "/bin/bash" ]
ENV APP_SETTINGS config.ProductionConfig
ENV FLASK_ENV production

CMD [ "/heimdal/startup.sh" ]
