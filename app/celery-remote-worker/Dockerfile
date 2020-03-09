FROM ubuntu:18.04

# Get the ODBC driver for Microsoft SQL Server and dependencies
RUN apt-get update \
&& apt-get install -y \
    python3-pip \
    python3-dev \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
&& curl https://packages.microsoft.com/config/debian/9/prod.list  > /etc/apt/sources.list.d/mssql-release.list \
&& apt-get update \
&& ACCEPT_EULA=Y apt-get -y install --no-install-recommends \
    msodbcsql17 \
    unixodbc \
    unixodbc-dev \
    libodbc1 \
    odbcinst1debian2 \
    odbcinst \
&& apt-get clean

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

CMD ["celery", "worker", "-A", "remote_worker", "-l", "INFO"]