#
# based on https://hub.docker.com/r/jjanzic/docker-python3-opencv/
#

FROM jjanzic/docker-python3-opencv

RUN mkdir /setup
WORKDIR /setup
ADD requirements.txt /setup/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6006

RUN useradd -m -U -s /bin/bash opencv
USER opencv
WORKDIR /home/opencv
ENV SHELL /bin/bash
