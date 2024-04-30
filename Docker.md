# Docker usefull commends 

## Basic interaction 

```bash
docker ps           # list all running process
docker image list   # list all createrd images
docker container list # list all built containers

docker stop <the-container-id> # stop container
docker rm <the-container-id> # remove container
docker image rm <the-image-id> # remove an image
```

### running a container (ubuntu specific)

``` bash
docker run -it --rm --gpus 'device=1' --shm-size 16G -v /media/sde1/multy:/workspace 8d981c027411 bash
```

- `-it`: create iteractive terminal
- `--rm`: remove container when exit 
- `--gpus`: allows GPU usage `--gpus=all` to se all other than specified
- `-v`: mount a dirctory to the container to store files. `<local-machine-directory>:<directory-in-contaienr>`
- `bash`: indicate create a bash terminal when start the container

## Save changed container as image
```bash
# docker commit -p <container_id> <new_container_name>
sudo docker commit -p 524aa76baafb myubuntu
```
This save the current running (changed) container as a new image call `myubuntu`

> **NOTE: When saving the container, do not save it when a volume is attached to it. Otherwise, it will save the attached volume as a part of the container as well. (unless you want to do this)**

## Dockerfile
### build image
```bash
cd <directory-containing-Dockerfile>
docker build -t <image-name> .
```

### create ubutnu image
```Dockerfile
## Docker file (ubuntu specific)
#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#

# Pull base image.
FROM ubuntu:20.04

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y curl git unzip vim nano wget  

# Add files.
ADD root/.bashrc /root/.bashrc
ADD root/.gitconfig /root/.gitconfig
ADD root/.scripts /root/.scripts

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
```