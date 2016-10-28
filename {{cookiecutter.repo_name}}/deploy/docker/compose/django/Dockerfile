FROM python:2.7.12-slim
ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./code /app
# COPY ~/.pip/pip.conf /.pip/pip.conf
# COPY ./requirements.txt /requirements.txt
COPY gunicorn.sh /gunicorn.sh
COPY entrypoint.sh /entrypoint.sh
COPY sources.list /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get -y upgrade
RUN apt-get install -y build-essential python-dev
RUN apt-get install -y libjpeg-dev libfreetype6-dev zlib1g-dev
RUN apt-get install -y python-psycopg2 postgresql-server-dev-all

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /app/requirements.txt

RUN groupadd -r django && useradd -r -g django django
RUN chown -R django /app

RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh

RUN chmod +x /entrypoint.sh && chown django /entrypoint.sh
RUN chmod +x /gunicorn.sh && chown django /gunicorn.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
