FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install -y python3-pip python3-dev \
&& apt-get clean

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

CMD ["celery", "worker", "-A", "remote_worker", "-l", "INFO"]