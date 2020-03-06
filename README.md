

## Running in docker:

### Prerequisites:

 - docker
 - docker-compose


### Run system (stable version)
#### Windows

```bash
cd docker
$env:ARCOR2_VERSION=$(cat ..\arcor2\VERSION)
docker-compose up
```

#### Linux

```bash
cd docker
export ARCOR2_VERSION=$(cat ../arcor2/VERSION)
sudo -E docker-compose up
```

### Run newest build
#### Windows

```bash
cd docker
$env:ARCOR2_VERSION="latest"
docker-compose up
```

#### Linux

```bash
cd docker
export ARCOR2_VERSION=latest
sudo -E docker-compose up
```

## Uploading services and object_types to project service
Use docker exec to attach to arserver container and run following scripts and restart arserver.
```bash
/root/arcor2_kinali/arcor2_kinali/services/upload.py
/root/arcor2_kinali/arcor2_kinali/object_types/upload.py
```


## Installation (for development without docker):
```bash
pip3 install -e arcor2_kinali
```

## Releasing a new version
 TBA
