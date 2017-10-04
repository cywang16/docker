#
#

FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 5000 8000
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# CMD FLASK_APP=hello.py flask run
