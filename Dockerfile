FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3-dev python3-pip \
    build-essential \
    cmake \
    swig \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY demo /tmp/work

RUN cd /tmp/work \
 && mkdir build \
 && cd build \
#  && cmake -DCMAKE_BUILD_TYPE=Debug .. \
 && cmake .. \
 && make \
 && make install \
 && echo "done"

