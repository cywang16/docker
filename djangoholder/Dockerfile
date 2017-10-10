#
# PYTHONUNBUFFERED: Force the binary layer of the stdout and stderr streams (which is available as their buffer attribute) to be unbuffered.
#
# Just run python: docker run -it --rm --name py_workplace python:3 bash

FROM python
ENV PYTHONUNBUFFERED 1
EXPOSE 5000 8000
RUN mkdir /setup
WORKDIR /setup
ADD requirements.txt /setup/
RUN pip install -r requirements.txt
# ADD . /code/

