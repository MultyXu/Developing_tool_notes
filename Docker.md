# Docker usefull commends 

## Basic interaction 

```bash
docker ps           # list all running process, `-a` option list all containers including stopped
docker image list   # list all createrd images
docker container list # list all built containers

docker stop <the-container-id> # stop container
docker rm <the-container-id> # remove container
docker image rm <the-image-id> # remove an image
```

### running a container (ubuntu specific)

``` bash
docker run -it --rm --name multy_ubuntu --gpus device=1 --shm-size 16G -v /media/sde1/multy:/workspace 8d981c027411 bash
```

- `-it`: create iteractive terminal
- `--rm`: remove container when exit 
- `--gpus`: allows GPU usage `--gpus all` to se all other than specified
- `-v`: mount a dirctory to the container to store files. `<local-machine-directory>:<directory-in-contaienr>`. You can specify multiple `-v` option to mount multiple folders
- `--name`: give the container a name if needed.
- `bash`: indicate create a bash terminal when start the container

## With vscode 
`cmd+shift+p` and select `Remote-containers: Attach to running Container`

## Save changed container as image
```bash
# docker commit -p <container_id> <new_container_name>:<tag>
sudo docker commit -p 524aa76baafb myubuntu:version2
```
This save the current running (changed) container as a new image call `myubuntu`
### change tag 
```
docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```
Usually give a image name, it will find the `latest` tag.

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
  apt-get install -y curl git unzip vim nano wget\
  apt install nvidia-driver-535 nvidia-dkms-535

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
```
## GUI on remote container over ssh
### For windows wsl2 
permit any client for connection, in `wsl2` run
```
xhost +
```

if you want to disable the permission, run 
```
xhost -
```

get the display parameter 
```
echo $DISDPLAY
```

start the container with x11 config 
```
docker run --net host -v /tmp/.X11-unix:/tmp/.X11-unix -it [image_id]
```

set the environment variable the same as wsl2 
```
export DISPLAY=:0 # depends on what parameter you get
```

test gui 
```
xeyes
```
### For windows
follow this link: https://medium.com/@potatowagon/how-to-use-gui-apps-in-linux-docker-container-from-windows-host-485d3e1c64a3

in order to show pyplot in pythong file use
```
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()
```
### For Macos
Download XQuartz using brew, in setting security, ensure "allow all connections"

run container with port forwarding
```
-p 8000:22
```

Install necessary dependencies
```
apt install xauth x11-apps openssh-server
```

in `/etc/ssh/sshd_config/` set 
```
X11Forwarding yes
X11UseLocalhost no
PermitRootLogin yes
PasswordAuthentication yes
```

restart the ssh service 
```
service ssh restart
# or
/etc/init.d/ssh restart
```

add password for root
```
passwd root
[ender password]
```

New session directly ssh into container
```
ssh -X root@[ip.address] -p 8000
```

Now the x11 should be working, test if working with xclock. When restart the container, remember to restart the ssh service as well.
