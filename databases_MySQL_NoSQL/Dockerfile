# Use the official image as a parent image.
FROM python:3.7.5-stretch

# install project requirements
COPY src/requirements.txt /tmp/requirements.txt
COPY ./test_couchbase.py ./test_couchbase.py
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

RUN apt-get update && apt-get -y install sudo
RUN apt-get update && apt-get install -y lsb-release && apt-get clean all

# install couchbase server 6.5
RUN curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-6-amd64.deb
RUN sudo dpkg -i ./couchbase-release-1.0-6-amd64.deb
RUN sudo apt-get update
RUN sudo apt-get install couchbase-server=6.5.0-4960-1

# install libcouchbase
RUN sudo apt-get install libcouchbase-dev libcouchbase2-bin build-essential -y

# install couchbase Python SDK
RUN sudo apt-get install build-essential python-dev python-pip -y
RUN sudo -H pip install couchbase

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080
