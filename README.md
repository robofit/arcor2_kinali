

## Running in docker:

### Prerequisites:

 - docker
 - docker-compose

### Logging to repositories (only once):
#### Windows 

 1. In docker desktop setting/Daemon add "office.kinalisoft.eu:8082" to insecure registries
 2. Restart docker (using docker desktop)
 3. _docker login office.kinalisoft.eu:8082 --username=fit  --password=FIT2019_
 4. _docker login --username=arcor2 --password heslo.arcor2_

#### Linux

 1. Edit or create file */etc/docker/deamon.json*
 2. Add: 
 {
"insecure-registries": ["office.kinalisoft.eu:8082" ]
}
3. _sudo /etc/init.t/docker restart_
4. _docker login office.kinalisoft.eu:8082 --username=fit  --password=FIT2019_
6. _docker login --username=arcor2 --password heslo.arcor2_


### Run system (stable version)
```bash
cd docker
export ARCOR2_VERSION=\$(cat ../arcor2/VERSION)
sudo -E docker-compose up
```

### Run newest build
```bash
cd docker
export ARCOR2_VERSION=latest
sudo -E docker-compose up
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

## Releasing a new version
1. Update version info
 2. Push all changes to arcor2_kinali repository
 3. Create tag/release with new version
 5. Build arcor2_kinali service with: _docker build . -f docker/Dockerfile-arserver -t arcor2/arcor2_arserver :\$(cat arcor2/VERSION) --build-arg version=\$(cat arcor2/VERSION)_
 6. Push service to dockerhub
	 7. docker push arcor2/arcor2_kinali:$(cat arcor2/VERSION)
