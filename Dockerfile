FROM python:3

RUN mkdir /opt/galaxy-merchant
COPY ./requirements.txt /opt/galaxy-merchant
WORKDIR /opt/galaxy-merchant
RUN pip install -r requirements.txt