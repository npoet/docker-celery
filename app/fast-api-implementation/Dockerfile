FROM python:3.7

# Get the ODBC driver for Microsoft SQL Server
RUN apt-get update \
&& apt-get install -y \
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
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY . /
WORKDIR /app/fast-api-implementation