#!/bin/bash 
VERSION=latest
docker build --no-cache -f Dockerfile-arserver -t arcor2/arcor2_arserver_kinali:$VERSION  ../ --build-arg version=$VERSION
docker build --no-cache -f Dockerfile-execution -t arcor2/arcor2_execution_kinali:$VERSION --build-arg version=$VERSION ../   
