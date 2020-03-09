FROM ubuntu:18.04

# Get the ODBC driver for Microsoft SQL Server and dependencies
RUN apt-get update \
&& apt-get install -y \
    python3-pip \
    python3-dev \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

RUN apt-get update
ENV ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive
RUN apt-get install mssql-tools unixodbc-dev -y

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN odbcinst -j
RUN cat /etc/odbcinst.ini

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

CMD ["uvicorn", "api_endpoints:API_app"]