FROM ubuntu:18.04
MAINTAINER prescheneder

COPY . .

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        python3 \
        python3-pip \
        python3-dev \
        build-essential \
        time \
        python3-pkg-resources \
        autotools-dev \
        autoconf \
        libboost-all-dev \
        muscle \
        wget \
    && pip3 --no-cache-dir install --upgrade \
        setuptools \
        wheel \
    && cd /qcat \
	&& pip3 --no-cache-dir install . \
	&& cd - \
	&& rm -rf /qcat \
	&& qcat -h \
    # Cleanup \
    && apt-get remove --purge -y \
        build-essential \
        python3-dev \
        autotools-dev \
        autoconf \
    && apt autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/*

CMD ./pipeline.sh > /data/log.txt
