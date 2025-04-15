docker run --name multy_ssc_ --entrypoint bash -dit --gpus device=all \
	-v ~/:/multy_vino \
    -v /media/sda1/multy:/workspace_sda \
    -v /media/sdc1/multy:/workspace_sdc \
    -v /media/sde1/multy:/workspace_sde \
    -v /media/sdd1:/Data_nuscenes \
    -v /media/sdb1:/Data_Carla \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    nvidia/cuda:11.6.1-runtime-ubuntu20.04
	# ssc:v3

# on vino