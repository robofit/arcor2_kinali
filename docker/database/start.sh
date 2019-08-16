#!/bin/bash  

cd /root/arcor2
git pull origin master
#cd /root/arcor2/arcor2/nodes/
mongod &
arcor2_persistent_storage
