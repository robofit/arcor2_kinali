#!/bin/bash 
/wait-for `echo $ARCOR2_PERSISTENT_STORAGE_URL`/projects 
arcor2_server
