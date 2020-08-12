#!/bin/bash 
VERSION=`python3 ../setup.py --version`
docker image push arcor2/arcor2_upload_kinali:$VERSION

