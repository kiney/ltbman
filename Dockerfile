FROM debian:jessie

ENV VERSION "1"

ENV DEBIAN_FRONTEND noninteractive

# install basic and VNC stuff
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    locales \
    unzip \
    python3-pip

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# install gunicorn
RUN pip3 install gunicorn

RUN useradd -ms /bin/bash ltb
RUN mkdir /var/lib/ltbman
RUN chown ltbman:ltbman /var/lib/ltbman


EXPOSE 8080
VOLUME ["/var/lib/ltbman"]

# Add Tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-amd64 /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

#RUN mkdir /opt/ltbman
ADD https://github.com/kiney/ltbman/archive/master.zip /opt/ltbman
#RUN mv /opt/ltbman-master /opt/ltbman
#ADD https://github.com/kiney/records/archive/master.zip /opt/ltbman-master
##RUN cd /opt/ltbman && git clone git@github.com:kiney/ltbman.git 

CMD ["/run.sh"]
