#!/bin/bash 
VERSION=`python3 ../setup.py --version`
BASE_VERSION=`cd ../../arcor2;python3 setup.py --version;cd - > /dev/null`
docker build --no-cache -f Dockerfile -t arcor2/arcor2_upload_kinali:$VERSION  ../ --build-arg version=$BASE_VERSION

