#!/bin/bash 
BASE_VERSION=0.5.1-beta.3
VERSION=0.5.1-beta.3
docker build --no-cache -f Dockerfile -t arcor2/arcor2_base_kinali:$VERSION  ../ --build-arg version=$BASE_VERSION
docker build --no-cache -f Dockerfile-arserver -t arcor2/arcor2_arserver_kinali:$VERSION  ../ --build-arg version=$VERSION
docker build --no-cache -f Dockerfile-execution -t arcor2/arcor2_execution_kinali:$VERSION --build-arg version=$VERSION ../   
