FROM python:2.7.12-slim
ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./ /app
COPY ./deploy/compose/django/pip.conf /root/.pip/pip.conf
COPY ./requirements.txt /requirements.txt
COPY ./deploy/compose/django/gunicorn.sh /gunicorn.sh
COPY ./deploy/compose/django/entrypoint.sh /entrypoint.sh
COPY ./deploy/compose/django/sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y build-essential python-dev apt-utils postgresql-server-dev-all libjpeg-dev libfreetype6-dev zlib1g-dev

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /requirements.txt

RUN groupadd -r django && useradd -r -g django django
RUN chown -R django /app

RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh

RUN chmod +x /entrypoint.sh && chown django /entrypoint.sh
RUN chmod +x /gunicorn.sh && chown django /gunicorn.sh

RUN rm -rf /app/Vagrantfile
RUN rm -rf /app/deploy
RUN rm -rf /app/.idea
RUN rm -rf /app/docs

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
