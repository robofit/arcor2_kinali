#!/bin/bash  
cd /root/arcor2_kinali/arcor2_kinali/services || exit
python upload.py
cd /root/arcor2_kinali/arcor2_kinali/object_types || exit
python upload.py
cd /root/arcor2/arcor2/user_objects || exit
python upload.py
arcor2_manager --rpc-plugins arcor2_kinali.plugins/KinaliRpcPlugin &
sleep 5
cd /root/arcor2 || exit
arcor2_server
