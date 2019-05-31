FROM python:3.7-alpine
COPY thing.py /usr/local/bin/thing.py
RUN  chmod +x /usr/local/bin/thing.py
CMD  ["/sbin/init"]