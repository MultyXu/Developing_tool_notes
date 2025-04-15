#!/bin/bash

# Prerequisites:
# - NVIDIA and NGC accounts created, docker container was build using the build_container.sh script
# - Install the nvidia-container-toolkit package
# - Install NVIDIA Driver 525 or 535 from NVIDIA
# - Install the NVIDIA packages for the above driver from the apt repository (for nvidia-smi)
# You can verify the prerequisites were successful by running nvidia-smi and checking
# that it actually completes and you see the driver number in the output


# Create the docker container with the NVIDIA options provided in documentation, plus
# proxy settings from LL
	# -e DISPLAY=$DISPLAY \
    # --network=host \
    #     -p 5901:5901 \
    # -p 8211:8211 \
# xhost +local:docker
docker run --name multy_tiamat_sg_nav_all --entrypoint bash -dit --gpus device=all \
	-e PRIVACY_CONSENT=Y \
	-e ACCEPT_EULA=Y \
	-v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
	-v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
	-v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
	-v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
	-v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
	-v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
	-v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
	-v ~/docker/isaac-sim/documents:/root/Documents:rw \
    -v ~/:/multy_vino \
    -v /media/sda1/multy:/workspace_sda \
    -v /media/sdc1/multy:/workspace_sdc \
    -v /media/sde1/multy:/workspace_sde \
    -v /media/sdd1:/workspace_sdd \
	tiamat:sg_nav_yhu_baseline

# Just printing some "I'm done now" messages
echo -e "\n\nDocker started - access the container with the following command:\n"
echo -e "docker exec -it tiamat bash -l"
echo -e "\n\nStop container with the following command:\n"
echo -e "docker stop tiamat"
echo -e "\n\nRestart container with the following command:\n"
echo -e "docker start tiamat"
echo -e "\n\nRemove container with the following command:\n"
echo -e "docker container rm tiamat"