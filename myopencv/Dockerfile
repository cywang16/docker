#
# based on https://hub.docker.com/r/jjanzic/docker-python3-opencv/
#

FROM python

RUN apt-get update && \
        apt-get install -y \
        build-essential \
        cmake \
        libgtk2.0-dev \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libjasper-dev \
        libavformat-dev \
        libpq-dev \
        libcanberra-gtk-module

RUN pip install numpy

WORKDIR /
RUN wget https://github.com/opencv/opencv/archive/3.4.0.zip \
&& unzip 3.4.0.zip \
&& mkdir /opencv-3.4.0/cmake_binary \
&& cd /opencv-3.4.0/cmake_binary \
&& cmake -DBUILD_TIFF=ON \
  -DBUILD_opencv_java=OFF \
  -DWITH_CUDA=OFF \
  -DENABLE_AVX=ON \
  -DWITH_OPENGL=ON \
  -DWITH_OPENCL=ON \
  -DWITH_IPP=ON \
  -DWITH_TBB=ON \
  -DWITH_EIGEN=ON \
  -DWITH_V4L=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \
  -DPYTHON_EXECUTABLE=$(which python3.6) \
  -DPYTHON_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \
&& make \
&& make install \
&& cd / \
&& rm 3.4.0.zip \
&& rm -r opencv-3.4.0

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt
# EXPOSE 6006

RUN useradd -m -U -s /bin/bash opencv
USER opencv
WORKDIR /home/opencv
ENV SHELL /bin/bash
