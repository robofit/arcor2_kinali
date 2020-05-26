#!/bin/bash 
docker image push arcor2/arcor2_base_kinali:`cat ../arcor2_kinali/VERSION`
docker image push arcor2/arcor2_arserver_kinali:`cat ../arcor2_kinali/VERSION`
docker image push arcor2/arcor2_execution_kinali:`cat ../arcor2_kinali/VERSION`

