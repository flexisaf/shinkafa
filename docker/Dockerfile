
############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:14.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Edache Peter

ENV DOCKYARD_HOME=/src
ENV DOCKYARD_SRC=/src/webapp/flexisaf
ENV DOCKYARD_VIRT=/src/webapp/virt
ENV DOCKYARD_VIRT_ACTIVATE=/src/webapp/virt/bin/activate
ENV NGINX_SITE=/etc/nginx/sites-enabled



# Update the default application repository sources list
RUN apt-get  update -y
RUN apt-get install python	--force-yes -y				## install 2.7
RUN apt-get install python-setuptools --force-yes -y 	## for python2.7 or above
RUN apt-get install build-essential --force-yes -y 		##
RUN apt-get install python-virtualenv --force-yes -y 	## virtual env
RUN apt-get install python-dev --force-yes -y 		## because ubuntu 14.04 does not have dev version of python 2
RUN apt-get install mysql-server --force -y
RUN apt-get install  build-essential \
                         libmysqlclient-dev \
                         libpq-dev \
                         nginx \
                         --force-yes -y

RUN apt-get install -y supervisor
RUN apt-get install python python-pip --force-yes -y
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade requests

WORKDIR $DOCKYARD_HOME

COPY SHINKAFA-0.0.1.tar.gz $DOCKYARD_SRC/

## remove default nginx config
# Set up NGINX
RUN rm /etc/nginx/sites-enabled/*
COPY 500.html $DOCKYARD_SRC/
COPY flexisaf-nginx.conf $NGINX_SITE/
COPY flexisaf-nginx.conf /etc/nginx/sites-available/

WORKDIR $DOCKYARD_SRC
RUN mkdir media  logs run
VOLUME ["$DOCKYARD_SRC/media/", "$DOCKYARD_SRC/logs/"]

RUN pip install  $DOCKYARD_SRC/SHINKAFA-0.0.1.tar.gz

EXPOSE 443

WORKDIR $DOCKYARD_SRC
COPY ./entry-point.sh /
ENTRYPOINT ["/entry-point.sh"]
