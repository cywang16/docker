#
# pygame on latest python
# X11 forwarding is based on https://github.com/sjawhar/udacity-mlnd-smartcab
#

FROM python

RUN pip install pygame

RUN useradd -m -U -s /bin/bash pygame
USER pygame
WORKDIR /home/pygame
ENV SHELL /bin/bash
