FROM python:3.8-alpine


COPY ../../resources/requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers postgresql-dev python3-dev musl-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir scripts
COPY ../../deployment/scripts scripts
RUN chmod +x /scripts/*

RUN mkdir src
COPY ../../src src
WORKDIR src

RUN set -ex && apk --no-cache add sudo
RUN apk --no-cache --update add libffi postgresql-libs gcc libc-dev
RUN apk update && apk add --no-cache supervisor

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chown -R 755 /vol/web
# USER user
USER root

CMD ["../scripts/entrypoint.sh"]
