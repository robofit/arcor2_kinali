
## Running in docker:

### Prerequisites:

 - docker
 - docker-compose

### Logging to repositories (only once):
#### Windows 

 1. In docker desktop settings set following: "insecure-registries": ["office.kinalisoft.eu:8082" ]
 2. Restart docker (using docker desktop)
 3. _docker login office.kinalisoft.eu:8082 --username=FIT2019  --password=FIT2019_
 4. _docker login --username=arcor2 --password heslo.arcor2_

#### Linux

 1. Edit or create file */etc/docker/deamon.json*
 2. Add: 
 {
"insecure-registries": ["office.kinalisoft.eu:8082" ]
}
3. _sudo /etc/init.t/docker restart_
4. _docker login office.kinalisoft.eu:8082 --username=FIT2019  --password=FIT2019_
6. _docker login --username=arcor2 --password heslo.arcor2_


### Run system
```bash
cd docker
docker-compose up
```

## Installation (for development without docker):
```bash
pip3 install -e swagger_client
pip3 install -e arcor2_kinali
```

## Usage:
```bash
arcor2_manager --rpc-plugins arcor2_kinali.plugins/KinaliRpcPlugin
```
