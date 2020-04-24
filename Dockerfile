FROM python:3.8-slim

RUN pip install flask
RUN pip install plexapi
RUN pip install pylogrus

WORKDIR /usr/bin/plex_webhook
COPY plex_webhook/ /usr/bin/plex_webhook
ENTRYPOINT [ "python" ]
CMD ["plex_webhook.py"]