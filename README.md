

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

## Installation (for development without docker):
```bash
pip3 install -e arcor2_kinali
```

## Usage:
```bash
./arcor2_kinali/services/upload.py
./arcor2_kinali/object_types/upload.py
```

## Releasing a new version
1. Update version info
 2. Push all changes to arcor2_kinali repository
 3. Create tag/release with new version
 5. Build arcor2_kinali service with: _docker build . -f docker/Dockerfile-arserver -t arcor2/arcor2_arserver :\$(cat arcor2/VERSION) --build-arg version=\$(cat arcor2/VERSION)_
 6. Push service to dockerhub
	 7. docker push arcor2/arcor2_kinali:$(cat arcor2/VERSION)
