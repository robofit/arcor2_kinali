#!/bin/bash 
/wait-for `echo $ARCOR2_PERSISTENT_STORAGE_URL`/projects 
cd /root/arcor2_kinali/arcor2_kinali/services || exit
python upload.py
cd /root/arcor2_kinali/arcor2_kinali/object_types || exit
python upload.py
cd /root/arcor2/arcor2/user_objects || exit
python upload.py
arcor2_server
